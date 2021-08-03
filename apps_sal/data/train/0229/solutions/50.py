class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        zcount = 0
        pos = []
        neg = []
        for n in A:
            if n == 0:
                zcount += 1
            elif n > 0:
                pos.append(n)
            else:
                neg.append(-n)

        def verifypos(A):
            count = collections.Counter(A)
            for x in sorted(A, key=abs):
                if count[x] == 0:
                    continue
                if count[2 * x] == 0:
                    return False
                count[x] -= 1
                count[2 * x] -= 1

            return True
        return verifypos(pos) and verifypos(neg)
