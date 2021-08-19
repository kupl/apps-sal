class Solution:

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # unique elms in list
        elms = set()

        # prevent dup. effort during consecutive search
        visited = set()
        max_consecutive = 0

        for num in nums:

            elms.add(num)

        # look for all unique consecutive subsequences
        for num in nums:

            if num in visited:

                continue

            visited.add(num)

            # elm by itself
            curr_consecutive = 1
            tmp = num - 1

            # number of consecutive elms before
            # this elm
            while tmp in elms:

                visited.add(tmp)
                curr_consecutive += 1
                tmp -= 1

            tmp = num + 1

            # number of consecutive elms after
            # this elm
            while tmp in elms:

                visited.add(tmp)
                curr_consecutive += 1
                tmp += 1

            if curr_consecutive > max_consecutive:

                max_consecutive = curr_consecutive

        return max_consecutive
