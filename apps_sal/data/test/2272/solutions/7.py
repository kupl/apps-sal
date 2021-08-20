class Interval:

    def __init__(self, a, b):
        self.interval_a = a
        self.interval_b = b

    def can_go(self, interval):
        return interval.interval_a < self.interval_a < interval.interval_b or interval.interval_a < self.interval_b < interval.interval_b


intervals = []
matrix = []


def dfs(a, b, visited, matrix):
    if a == b:
        return True
    ans = False
    visited[a] = True
    for i in range(len(matrix)):
        if matrix[a][i] and (not visited[i]):
            ans = ans or dfs(i, b, visited, matrix)
    return ans


for i in range(int(input())):
    (t, a, b) = list(map(int, input().split()))
    if t == 1:
        newInterval = Interval(a, b)
        intervals.append(newInterval)
        for row in range(len(matrix)):
            matrix[row].append(intervals[row].can_go(newInterval))
        matrix.append([])
        for col in range(len(matrix)):
            matrix[len(matrix) - 1].append(newInterval.can_go(intervals[col]))
    if t == 2:
        visited = []
        for i in range(len(intervals)):
            visited.append(False)
        if dfs(a - 1, b - 1, visited, matrix):
            print('YES')
        else:
            print('NO')
