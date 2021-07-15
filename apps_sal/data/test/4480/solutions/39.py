class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        average, part, cnt = sum(A) // 3, 0, 0
        for a in A:
            part += a
            if part == average:
                cnt += 1
                part = 0
        return cnt >= 3

