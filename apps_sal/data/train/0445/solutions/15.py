class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        mins, maxs = nums[:4], nums[:4]
        for num in nums[4:]:
            mins.append(num)
            mins.sort()
            mins.pop()
            maxs.append(num)
            maxs.sort(reverse=True)
            maxs.pop()
        maxs = maxs[::-1]
        '''
\t\tmins[i] maxs[j]
        i j
        0 0 
        1 1 
        2 2 
        3 3 
        '''
        return min(maxs[i] - mins[i] for i in range(4))


'''
Input 1: [1,5,0,10,14], all maxs and mins are not overlapped
maxs [1, 5, 10, 14]
mins [0, 1, 5, 10]
diff [1, 4, 5, 4]

Input 2: [1,1,2,3,4], maxs and mins are overlapped
maxs [1, 2, 3, 4]
mins [1, 1, 2, 3]
diff [0, 1, 1, 1]
'''
