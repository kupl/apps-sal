class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:

        total = sum(A)

        if total % 3 != 0:
            return False

        target = total / 3
        print(target)

        temp = 0
        res = []
        for i, v in enumerate(A):
            temp = temp + v

            if temp == target:
                res.append(i)
                temp = 0
        print(res)

        return len(res) >= 3
