class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        freq = dict()
        for i in A:
            freq[i] = freq.get(i, 0) + 1

        for k in sorted(list(freq.keys()), key=lambda x: abs(x)):
            if freq[k] == 0: continue
            if freq[k] > freq.get(2*k, 0):
                return False
            freq[2*k] -= freq[k]
            
        return True

