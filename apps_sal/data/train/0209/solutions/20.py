class Solution:

    def mergeStones(self, stones, k):
        if (len(stones) - 1) % (k - 1):
            return -1
        cost = [[None] * len(stones) for _ in stones]

        def subCost(left, right):
            if left == right:
                return 0
            if cost[left][right] != None:
                return cost[left][right]
            if right - left + 1 == k:
                cost[left][right] = sum(stones[left:right + 1])
                return cost[left][right]
            divs = [left + i for i in range(k + 1)]
            divs[-1] = right + 1

            def moveDividers():

                def moveDivider(i):
                    if i == 0:
                        return False
                    if divs[i] == right - (k - 1 - i):
                        return moveDivider(i - 1)
                    divs[i] += 1
                    while (divs[i] - divs[i - 1] - 1) % (k - 1):
                        divs[i] += 1
                    for j in range(i + 1, len(divs) - 1):
                        divs[j] = divs[j - 1] + 1
                    return True
                return moveDivider(len(divs) - 2)
            best = float('inf')
            while 1:
                subSum = 0
                for div_i in range(len(divs) - 1):
                    subSum += subCost(divs[div_i], divs[div_i + 1] - 1)
                best = min(best, subSum)
                if not moveDividers():
                    break
            result = best + sum(stones[left:right + 1])
            cost[left][right] = result
            return result
        result = subCost(0, len(stones) - 1)
        return result
