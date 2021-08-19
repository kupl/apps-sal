class Solution:
    def findLatestStep(self, A: List[int], m: int) -> int:
        n = len(A)
        arr = [0] * n
        parent = [i for i in range(n)]
        rank = [1] * n
        groupSize = [0] * n
        groupMap = set()
        ans = -1

        def ugm(x):
            nonlocal m
            if groupSize[x] == m:
                groupMap.add(x)
            else:
                if x in groupMap:
                    groupMap.remove(x)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def join(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                if px < py:
                    parent[py] = px
                    groupSize[px] += groupSize[py]
                    groupSize[py] = 0
                else:
                    parent[px] = py
                    groupSize[py] += groupSize[px]
                    groupSize[px] = 0
                ugm(px)
                ugm(py)

        for ind, num in enumerate(A):
            num -= 1
            arr[num] = 1
            groupSize[num] = 1
            ugm(num)
            # print(arr)
            if num - 1 >= 0 and arr[num - 1]:
                join(num - 1, num)

            if num + 1 < n and arr[num + 1]:
                join(num, num + 1)
            # print(groupMap)
            if len(groupMap) > 0:
                ans = ind + 1
        return ans
