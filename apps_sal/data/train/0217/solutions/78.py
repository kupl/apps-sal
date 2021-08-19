class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        dp = []
        for i in range(len(A)):
            if i == 0:
                dp.append(set([A[i]]))
            else:
                inner = set([A[i]])
                for d in dp[-1]:
                    inner.add(d | A[i])
                dp.append(inner)
        total = set()
        for d in dp:
            total.update(d)
        return len(total)
