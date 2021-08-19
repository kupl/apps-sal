class Solution:

    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if not wall:
            return 0
        hsh = collections.defaultdict(int)
        for row in wall:
            distance_from_left = 0
            for brick_width in row[:-1]:
                distance_from_left += brick_width
                hsh[distance_from_left] += 1
        return len(wall) - max(list(hsh.values()) + [0])
