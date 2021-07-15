class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l = []
        for x in arr:
            if not l or x >= l[-1]:
                l.append(x)
            else:
                break
        r = []
        for i in range(len(arr)-1, -1, -1):
            if not r or arr[i] <= r[-1]:
                r.append(arr[i])
            else:
                break
        r.reverse()
        if len(l) == len(arr):
            return 0
        sol = max(len(l), len(r))
        i, j = 0, 0
        # print(l, r)
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                i += 1
            else:
                while j < len(r) and l[i] > r[j]:
                    j += 1
            # print(i, j)
            sol = max(sol, i+len(r)-j)
        return len(arr) - sol
