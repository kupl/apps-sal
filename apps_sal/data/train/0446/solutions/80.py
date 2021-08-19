class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        H = dict()
        for element in arr:
            if element in H:
                H[element] += 1
            else:
                H[element] = 1
        H = {k: v for (k, v) in sorted(list(H.items()), key=lambda item: item[1])}
        S = 0
        M = len(H)
        c = 0
        for val in list(H.values()):
            S += val
            c += 1
            if S == k:
                return M - c
            elif S > k:
                return M - c + 1
            else:
                continue
