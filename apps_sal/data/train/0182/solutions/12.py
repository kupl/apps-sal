class Solution:

    def get_empty_per_level(self, height, level):
        print(("Level: ", level))
        block_start = 0
        n = len(height)
        while block_start < n and height[block_start] < level:
            block_start += 1

        if block_start == n:
            print("No start")
            return n

        block_end = n - 1
        while block_end > block_start and height[block_end] < level:
            block_end -= 1

        if block_end == block_start:
            print("No end")
            return n - 1

        print("Some value")
        return n - (block_end - block_start + 1)

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height or len(height) == 0:
            return 0

        levels = set(height)
        levels = list(levels)

        if 0 in levels:
            levels.remove(0)

        levels.sort()

        if len(levels) == 0:
            return 0

        max_level = max(height)
        total_count = sum([max_level - item for item in height])

        prev_level = levels.pop(0)
        missing_water_per_level = self.get_empty_per_level(height, prev_level)
        total_count -= prev_level * missing_water_per_level
        for level in levels:
            missing_water_per_level = self.get_empty_per_level(height, level)
            multi_level_count = (level - prev_level) * missing_water_per_level
            total_count -= multi_level_count
            #print("Level: ", level, " count after: ", total_count, "missing water: ", missing_water_per_level)

            prev_level = level

        return total_count
