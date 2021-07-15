from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # we keep two pointers and we keep track of min and max between those pointers
        # if the new number being added is having difference from both min and max within the range we increase j and update min and max if necessary else we increase i till we get the difference less than target while changing i and also we keep on updating the min and max
        # it can mark the beginning of a new sub array
        # however if we can make this update faster constant time and at max we need to increase i from i to j by deleting each number then also it is in worse case O(nk) instead of linear we can save sometime
        # we do not need indices and so we can use SortedList instead of SortedDict to make processing of finding min and max after changing i faster
        s = SortedList()
        # we keep on adding new values to the sortedList and when we get max - min greater than target then we keep on removing values from the list till the sorted list becomes valid again
        max_length = 0
        j = 0
        for i in range(len(nums)):
            s.add(nums[i])
            while s and s[-1] - s[0] > limit:
                s.remove(nums[j])
                j += 1
            max_length = max(max_length,i-j + 1)
        return max_length
        
        
        
        
        # for the following approach also the time limit gets exceeded because although operations on dictionary are O(logn) we are doing them for more number of times then expected
        '''
        # i.e. if min is our problem then we need to increase i till we find new min 
        # i.e we need to start from i = i + max_index of current_min
        # and if max is our problem then we need to increase i till we find new max
        # i.e we need to start from i = i + max_index of current_max
        # and if both are a problem then we need to increase i till max when both are changed
        # this we can do if we use a hashmap mapping each value from i to j with its max index in the array we do not care for intermediate indices
        max_length = -float('inf')
        mapping = SortedDict()
        Min = nums[0]
        Max = nums[0]
        mapping[Min] = 0
        i = 0
        while i < len(nums):
            j = i
            # print('a',i,j,Max,Min)
            while j < len(nums) and abs(nums[j] - Min) <= limit and abs(nums[j] - Max) <= limit:
                Max = max(Max,nums[j])
                Min = min(Min,nums[j])
                # we are just concerned with the max value
                mapping[nums[j]] = j
                j += 1
                max_length = max(max_length,j - i)
                
            # print('b',i,j,Min,Max)
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
                    # after each update we need to update min and max and the following steps will take O(n)
                    Min = mapping.peekitem(0)[0]
                    Max = mapping.peekitem()[0]
                    while mapping[Min] < i:
                        del mapping[Min]
                        Min = mapping.peekitem(0)[0]
                    while mapping[Max] < i:
                        del mapping[Max]
                        Max = mapping.peekitem()[0]
                    
                # print(mapping)
                # print('c',i,j,Max,Min)
        return max_length
        
        '''
        # for the following approach time limit gets exceeded
        '''
        max_length = -float('inf')
        Min = nums[0]
        Max = nums[0]
        i = 0
        while i < len(nums):
            j = i 
            #print('a',i,j,Max,Min)
            while j < len(nums) and abs(nums[j] - Min) <= limit and abs(nums[j] - Max) <= limit:
                Max = max(Max,nums[j])
                Min = min(Min,nums[j])
                j += 1
                max_length = max(max_length,j - i)
            #print('b',i,j,Max,Min,len(nums))
            if j >= len(nums)-1:
                break
            else:
                while i < j and nums[i] != Min and nums[i] != Max:
                    i += 1
                while i < j and (abs(nums[j] - Min) > limit or abs(nums[j] - Max) > limit):
                    i += 1
                    #print(i)
                    Min = min(nums[i:j+1])
                    Max = max(nums[i:j+1])
                    #print('c',i,j,Max,Min)
        return max_length
        '''            
        
        
        

