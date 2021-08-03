class Solution:
    def maxJumps(self, arr: List[int], dis: int) -> int:
        res = 1
        d = dict()
        visit = set()

        if len(arr) == 1:
            return 1

        for i in range(len(arr)):
            if i == 0:
                if arr[i] <= arr[i + 1]:
                    d[i] = 1
                    visit.add(i)
            elif i == len(arr) - 1:
                if arr[i] <= arr[i - 1]:
                    d[i] = 1
                    visit.add(i)
            else:
                if arr[i] <= arr[i - 1] and arr[i] <= arr[i + 1]:
                    d[i] = 1
                    visit.add(i)

        def dfs(index):
            if index not in visit:
                visit.add(index)
                cur = 1
                for i in range(1, dis + 1):
                    if index - i >= 0 and arr[index - i] < arr[index]:
                        temp = dfs(index - i)
                        d[index - i] = temp
                        cur = max(cur, 1 + temp)
                    else:
                        break
                for i in range(1, dis + 1):
                    if index + i < len(arr) and arr[index + i] < arr[index]:
                        temp = dfs(index + i)
                        d[index + i] = temp
                        cur = max(cur, 1 + temp)
                    else:
                        break
                return cur
            else:
                return d[index]

        for x in range(len(arr)):
            if x not in visit:
                cur = dfs(x)
                d[x] = cur
                res = max(res, cur)
            else:
                res = max(res, d[x])

        return res
