from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minheap = [[nums[0], 0]]
        maxheap = [[-nums[0], 0]]
        left = -1
        res = 1
        for i, val in enumerate(nums[1:]):
            j = i + 1
            while len(maxheap) and len(minheap) and max(val, -maxheap[0][0]) - min(val, minheap[0][0]) > limit:
                if val == max(val, -maxheap[0][0]):
                    v, l = heapq.heappop(minheap)
                if minheap and val == min(val, minheap[0][0]):
                    v, l = heapq.heappop(maxheap)
                left = max(l, left)
            res = max(j - left, res)
            heapq.heappush(minheap, [val, j])
            heapq.heappush(maxheap, [-val, j])
        return res

        '''
        s = SortedList()
        max_length = 0
        j = 0
        for i in range(len(nums)):
            s.add(nums[i])
            while s and s[-1] - s[0] > limit:
                s.remove(nums[j])
                j += 1
            max_length = max(max_length,i-j + 1)
        return max_length
        '''
        '''
        max_length = -float('inf')
        mapping = SortedDict()
        Min = nums[0]
        Max = nums[0]
        mapping[Min] = 0
        i = 0
        while i < len(nums):
            j = i
            while j < len(nums) and abs(nums[j] - Min) <= limit and abs(nums[j] - Max) <= limit:
                Max = max(Max,nums[j])
                Min = min(Min,nums[j])
                mapping[nums[j]] = j
                j += 1
                max_length = max(max_length,j - i)
                
            if j >= len(nums)-1:
                break
            else:
                mapping[nums[j]] = j
                while i <= j and (abs(nums[j] - Min) > limit or abs(nums[j] - Max) > limit):
                    if abs(nums[j] - Min) > limit and abs(nums[j] - Max) > limit:
                        i = max(i,max(mapping[Min],mapping[Max]) + 1)
                        del mapping[Max]
                        if Min in mapping.keys():
                            del mapping[Min]

                    elif abs(nums[j] - Min) > limit:
                        i = max(i,mapping[Min] + 1)
                        del mapping[Min]
                        
                    elif abs(nums[j] - Max) > limit:
                        i = max(i,mapping[Max] + 1)
                        del mapping[Max]
                    Min = mapping.peekitem(0)[0]
                    Max = mapping.peekitem()[0]
                    while mapping[Min] < i:
                        del mapping[Min]
                        Min = mapping.peekitem(0)[0]
                    while mapping[Max] < i:
                        del mapping[Max]
                        Max = mapping.peekitem()[0]
                    
        return max_length
        
        '''
        '''
        max_length = -float('inf')
        Min = nums[0]
        Max = nums[0]
        i = 0
        while i < len(nums):
            j = i 
            while j < len(nums) and abs(nums[j] - Min) <= limit and abs(nums[j] - Max) <= limit:
                Max = max(Max,nums[j])
                Min = min(Min,nums[j])
                j += 1
                max_length = max(max_length,j - i)
            if j >= len(nums)-1:
                break
            else:
                while i < j and nums[i] != Min and nums[i] != Max:
                    i += 1
                while i < j and (abs(nums[j] - Min) > limit or abs(nums[j] - Max) > limit):
                    i += 1
                    Min = min(nums[i:j+1])
                    Max = max(nums[i:j+1])
        return max_length
        '''
