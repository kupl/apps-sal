class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        A = dict(Counter(arr))
        B = [(item, A[item]) for item in A]
        B.sort(key=lambda x: x[1], reverse=True)
        result = len(B)
        while k > 0:
            if k >= B[-1][1]:
                k -= B[-1][1]
                result -= 1
                B.pop()
            else:
                k = 0
        return result
