class Solution:

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if sum(A) % 3 != 0:
            return False
        req = sum(A) // 3
        s = 0
        c = 0
        print(sum(A))
        print(req)
        for i in A:
            s += i
            if s == req:
                s = 0
                c += 1
        return c >= 3
