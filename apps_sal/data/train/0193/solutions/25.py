import collections

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = collections.Counter(arr)
        comp = [(freq[key],key) for key in freq]
        comp.sort(reverse=True)
        target = len(arr)/2
        index,curr_sum = 0,0
        while index < len(comp) and curr_sum < target:
            curr_sum += comp[index][0]
            index +=1
        return index
