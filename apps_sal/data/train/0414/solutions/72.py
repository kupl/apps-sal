class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        c = {}
        maxarray = max(arr)
        while max(list(c.values()), default=-1) < k:
            if arr[0] != maxarray:
                (arr[0], lastItem) = (max(arr[0], arr[1]), min(arr[0], arr[1]))
                arr.pop(1)
                arr.append(lastItem)
                if arr[0] not in c:
                    c[arr[0]] = 1
                else:
                    c[arr[0]] += 1
            else:
                return arr[0]
        for (i, val) in list(c.items()):
            if val >= k:
                return i
        return -1
