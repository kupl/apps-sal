class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for (i, e) in enumerate(nums):
            print('fe')
            if e in table:
                table[e] = [table[e][0] + 1, table[e][1] + [i]]
            else:
                table[e] = [1, [i]]
            sub_target = target - e
            if sub_target in table and (sub_target != e or table[sub_target][0] >= 2):
                print(table)
                first_idx = i
                second_idx = None
                for index in table[sub_target][1]:
                    if index != first_idx:
                        second_idx = index
                        break
                assert (second_idx, 'got shit')
                result = [first_idx, second_idx]
                result.sort()
                return result
        return []
