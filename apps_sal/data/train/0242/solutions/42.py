class Solution:
    # O(n) time, O(n) space
    def maxEqualFreq(self, nums: List[int]) -> int:
        count2num = defaultdict(set)
        num_count = Counter()
        max_len = 0
        
        def is_valid(count2num):
            counts = list(count2num.keys())
            # each element appears only once, or there is only 1 kind of element 
            if len(counts) == 1 and (counts[0] == 1 or len(count2num[counts[0]]) == 1):
                return True
            # Otherwise, if there are not 2 different counts, this prefix should be invalid
            if len(counts) != 2:
                return False
            # 2 different counts
            counts.sort()
            # Only 1 element has count 1, and others have a same different count
            if counts[0] == 1 and len(count2num[1]) == 1:
                return True
            # Two consecutive counts, and the larger one only has 1 element
            if counts[0] + 1 == counts[1] and len(count2num[counts[1]]) == 1:
                return True
            
            return False
        
        for i in range(len(nums)):
            num = nums[i]
            num_count[num] += 1
            count = num_count[num]
            count2num[count].add(num)
            if count > 1:
                count2num[count - 1].remove(num)
                if not count2num[count - 1]:
                    count2num.pop(count - 1)
            if is_valid(count2num):
                max_len = max(max_len, i + 1)
        
        return max_len
