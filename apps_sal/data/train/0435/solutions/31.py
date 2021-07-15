import collections
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        rem_array = [0]
        for num in A:
            rem_array.append((num+rem_array[-1])%K)
        
        counter = collections.Counter(rem_array)
        return sum(v*(v-1)//2 for v in counter.values())
