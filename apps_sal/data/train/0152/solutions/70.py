class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        #         1 2 3 4 5 6 7
        #         | | | |     |
        #         b     b     b
        #         forces: 3, 3, 6
        #         results = 3

        #         1 2 3 4 5 ...... 100000000  m = 2
        #         | | | | |            |
        #         b                    b
        #         result = 100000000 - 1

        #         1 2 3 4 5 ...... 100    m = 3
        #         | | | | |         |
        #         b                 b
        #               mid =  50
        # distance = 0 1 2 3 4 99
        #
        #                mid = 25
        # distance = 0 1 2 3 4 99
        #                mid = 11
        # distance = 0 1 2 3 4 99
        #                mid = 5
        # distance = 0 1 2 3 4 99
        #                mid = 4
        # distance = 0 1 2 3 4 99

        #         1 2 3 4 5 ...... 100    m = 4
        #         | | | | |         |
        #         b                 b
        #               mid =  50
        # distance = 0 1 2 3 4 99
        #
        #                mid = 25
        # distance = 0 1 2 3 4 99
        #                mid = 12
        # distance = 0 1 2 3 4 99
        #                mid = 6
        # distance = 0 1 2 3 4 99
        #                mid = 3
        # distance = 1 2 3 1 96
        # mid = 1
        # mid = 2

        def find_distance(mid_pos):

            count = 1
            pre = position[0]
            for i in range(1, len(position)):
                distance = position[i] - pre
                if distance >= mid_pos:
                    count += 1
                    pre = position[i]
            return count

        position = sorted(position)
        lo = 0
        hi = position[-1]
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if find_distance(mid) >= m:
                lo = mid + 1
            else:
                hi = mid - 1

        return hi
