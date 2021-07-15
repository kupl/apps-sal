class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        if A == B:
            return 0
        dp = [B]
        visit = {B}
        k = 0
        while dp:
            k += 1
            l = len(dp)
            for i in range(l):
                s = dp.pop()
                for j, c in enumerate(A):
                    if c != s[j]:
                        for n in range(j+1, len(A)):
                            if s[n] == c:
                                newS = s[0:j] + s[n] + s[j+1:n] + s[j] + s[n+1:]
                                if newS not in visit:
                                    if newS == A:
                                        return k
                                    dp.insert(0, newS)
                                    visit.add(newS)
                        break
