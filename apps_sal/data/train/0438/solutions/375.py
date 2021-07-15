class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        def find_set(x):
            if parents[x][0] == x:
                return x
            else:
                return find_set(parents[x][0])


        def union_set(x, y):
            x_root = find_set(x)
            y_root = find_set(y)
            parents[y_root][1] += parents[x_root][1]
            parents[x_root][0] = y_root


        n = len(arr)
        parents = [[i, 1] for i in range(n)]
        visited = [False for i in range(n)]
        answer = -1
        d = {}
        for i in range(n):
            num = arr[i] - 1
            visited[num] = True
            if num > 0 and visited[num - 1]:
                d[parents[find_set(num - 1)][1]] -= 1
                union_set(num - 1, num)
            if num + 1 < n and visited[num + 1]:
                d[parents[find_set(num + 1)][1]] -= 1
                union_set(num + 1, num)
            d[parents[num][1]] = 1 if parents[num][1] not in d else d[parents[num][1]] + 1
            if m in d and d[m] > 0:
                answer = i + 1
        return answer
