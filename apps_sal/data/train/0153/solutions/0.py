class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 4:
            return False

        length = sum(nums)
        if length % 4:
            return False
        length = (int)(length / 4)

        nums.sort(reverse=True)
        # print(nums)

        if length < nums[0]:
            return False
        elif length == nums[0]:
            stack = list([(set([0]), 1, length, 1)])
        else:
            stack = list([(set([0]), 1, length - nums[0], 2)])  # (usedIndexSet, searchStartFromIndex, target, remainRounds)
        while stack:
            usedSet, startIndex, target, remainRounds = stack.pop()
            #print(usedSet, set(range(0, len(nums))) - usedSet, target, remainRounds)
            for i in range(len(nums) - 1, startIndex - 1, -1):
                if i in usedSet:
                    continue
                num = nums[i]
                if num < target and i + 1 < len(nums):
                    stack.append((usedSet | {i}, i + 1, target - num, remainRounds))
                elif num == target:
                    if remainRounds == 0:
                        return True
                    else:
                        stack.append((usedSet | {i}, 1, length, remainRounds - 1))
                # Else not valid path, continue
        return False
