class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        mod = 10**9 + 7
        processed = dict()
        res = 0
        for a in sorted(A):
            counter = 1
            for key, val in list(processed.items()):
                key2 = a / key
                val2 = processed.get(key2, 0)
                if val2 != 0:
                    counter = (counter + val * val2) % mod
            processed[a] = counter
            res = (res + counter) % mod
        return res
            
            

