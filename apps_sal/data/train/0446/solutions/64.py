class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arr.sort()
        occ = []
        count = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                count += 1
            else:
                occ.append(count)
                count = 1
        occ.append(count)
        occ.sort()
        res = len(occ)
        for i in occ:
            if i <= k:
                res -= 1
                k -= i
            else:
                break
        return res
