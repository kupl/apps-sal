class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        res = xors = 0
        freq = collections.defaultdict(int, {0:1})
        _sum = collections.defaultdict(int)
        for i in range(n):
            xors ^= arr[i]
            res += freq[xors] * i - _sum[xors]
            freq[xors] += 1
            _sum[xors] += i+1
                
        return res
                

