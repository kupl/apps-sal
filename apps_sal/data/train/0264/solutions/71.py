class Solution:
    def maxLength(self, arr: List[str]) -> int:

        def dfs(start, seen):
            nonlocal res
            if start == len(arr):
                res = max(res, sum(len(arr[i]) for i in seen))
            else:
                is_end = True
                for i in graph[start]:
                    if all(len(arr[j].intersection(arr[i])) == 0 for j in seen):
                        is_end = False
                        seen.append(i)
                        dfs(i, seen)
                        seen.pop()
                if is_end:
                    res = max(res, sum(len(arr[i]) for i in seen))

        arr = [item for item in arr if len(item) == len(set(item))]
        arr = list(map(set, arr))
        graph = collections.defaultdict(list)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if len(arr[i].intersection(arr[j])) == 0:
                    graph[i].append(j)
        print((dict(graph)))

        res = 0
        for i in range(len(arr)):
            dfs(i, [i])
        return res
