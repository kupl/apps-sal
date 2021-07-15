class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        P = [0]
        for x in A:
            P.append((P[-1] + x) % K)
            
        # print(P)

        count = collections.Counter(P)
        
        # print(count)
        return sum(v*(v-1)//2 for v in count.values())
