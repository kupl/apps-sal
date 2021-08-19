import time


def getIntList():
    return list(map(int, input().split()))


def getTransIntList(n):
    first = getIntList()
    m = len(first)
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        result[i][0] = first[i]
    for j in range(1, n):
        curr = getIntList()
        for i in range(m):
            result[i][j] = curr[i]
    return result


n, k = getIntList()
a = getIntList()
# sums[i][j] - сумма a по индексам от i до j не включая j
sums = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(i + 1, n + 1):
        sums[i][j] = sums[i][j - 1] + a[j - 1]


class SearchProblem:
    def __init__(self, a, n, k, tiLim):
        self.a = a
        self.n = n
        self.k = k
        self.maxResult = 0
        self.tiLim = time.time() + tiLim

    def search(self, currResult, currIndex, currLines):
        # Время вышло - заканчиваем.
        if time.time() > self.tiLim:
            return
        if currLines > 0 and currResult <= self.maxResult:
            return
        if currLines == self.k - 1:
            lastSum = sums[currIndex][self.n]
            currResult = currResult & lastSum
            if currResult > self.maxResult:
                self.maxResult = currResult
        for nextIndex in range(currIndex + 1, self.n + 1):
            currSum = sums[currIndex][nextIndex]
            if currLines == 0:
                nextResult = currSum
            else:
                nextResult = currResult & currSum
            self.search(nextResult, nextIndex, currLines + 1)
        flag = True
        if time.time() > self.tiLim:
            flag = False
        return self.maxResult, flag


# upLim[i][j] - оценка сверху на красоту разбиения книг с номерами с j до конца по i полкам
upLim = [[0] * (n + 1) for _ in range(k + 1)]
for i in range(1, k + 1):
    if i == 1:
        for j in range(0, n):
            upLim[i][j] = sums[j][n]
    else:
        for j in range(n - i, -1, -1):
            upLim[i][j] = 0
            for j1 in range(j + 1, n):
                curr = min(sums[j][j1], upLim[i - 1][j1])
                upLim[i][j] = max(upLim[i][j], curr)


def solve():
    # Сначала ищем начальное решение deepfirst
    problem = SearchProblem(a, n, k, 0.1)
    if k == 1:
        return sum(a)
    maxResult, solved = problem.search(0, 0, 0)
    if solved:
        #print("deep first succeed")
        return maxResult
    results = [[set() for _ in range(n + 1)] for _ in range(k + 1)]
    # А теперь ищем полное решение динамическим программированием
    for i in range(1, n + 1):
        for firstIndexSum in range(0, i):
            # print(firstIndexSum, i);
            currSum = sums[firstIndexSum][i]
            if firstIndexSum == 0:
                if currSum > maxResult:
                    results[1][i].add(currSum)
                if k == 2:
                    lastSum = sums[i][n]
                    currResult = currSum & lastSum
                    if currResult > maxResult:
                        maxResult = currResult
                        for lines1 in range(k):
                            for j in range(n):
                                results[lines1][j] = {r for r in results[lines1][j] if r >= maxResult}
            else:
                for lines in range(k):
                    for prevSum in results[lines][firstIndexSum]:
                        # print(prevSum,"&",currSum,"=",prevSum&currSum)
                        fullSum = prevSum & currSum
                        currLines = lines + 1
                        if currLines == k - 1:
                            lastSum = sums[i][n]
                            currResult = fullSum & lastSum
                            if currResult > maxResult:
                                maxResult = currResult
                                for lines1 in range(k):
                                    for j in range(n):
                                        results[lines1][j] = {r for r in results[lines1][j] if r >= maxResult}
                        if upLim[k - currLines][i] <= maxResult:
                            continue
                        if fullSum > maxResult:
                            results[currLines][i].add(fullSum)
                        # print(i, results[i])

    return maxResult


print(solve())
