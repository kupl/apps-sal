class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:

        # P[i] stores sum up to index i
        P = [0]
        for x in A:
            P.append((P[-1] + x) % K)

        count = collections.Counter(P)

        ans = 0
        for v in list(count.values()):
            ans += int(v * (v - 1) * 0.5)

        return ans
        # return sum( v*(v-1)//2 for v in count.values())
