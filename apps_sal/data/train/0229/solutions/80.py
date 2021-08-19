class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        c = collections.Counter(A)
        for i in sorted(A, key=abs):
            if c[i] and c[i * 2]:
                c[i] -= 1
                c[i * 2] -= 1
        return all((c[i] == 0 for i in A))
