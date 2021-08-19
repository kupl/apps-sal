class Solution:

    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        (mins, maxs) = (nums[:4], nums[:4])
        for num in nums[4:]:
            mins.append(num)
            mins.sort()
            mins.pop()
            maxs.append(num)
            maxs.sort(reverse=True)
            maxs.pop()
        maxs = maxs[::-1]
        '\n\t\tmins[i] maxs[j]\n        i j\n        0 0 # change the largest 3 numbers to the 4-th largest, smallest numbers unchanged\n        1 1 # change the smallest number to the 2nd smallest, change the 2 largest to 3rd largest\n        2 2 # change the smallest 2 numbers to 3rd smallest, change the largest to 2nd largest\n        3 3 # change the smallest 3 numbers to 4th smallest,largest number unchanged\n        '
        return min((maxs[i] - mins[i] for i in range(4)))


'\nInput 1: [1,5,0,10,14], all maxs and mins are not overlapped\nmaxs [1, 5, 10, 14]\nmins [0, 1, 5, 10]\ndiff [1, 4, 5, 4]\n\nInput 2: [1,1,2,3,4], maxs and mins are overlapped\nmaxs [1, 2, 3, 4]\nmins [1, 1, 2, 3]\ndiff [0, 1, 1, 1]\n'
