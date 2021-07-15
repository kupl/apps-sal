class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        if not arr: return 0
        int_freq = collections.Counter(arr)
        size = len(arr)
        cur_size = size
        
        count = 0
        for num, freq in int_freq.most_common():
            cur_size -= freq
            count += 1
            if cur_size <= size // 2:
                return count
