class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        candy_count = 0
        my_boxes = initialBoxes
        my_keys = []

        while my_boxes:
            l = len(my_boxes)
            opened_new = False
            for b_i in range(l - 1, -1, -1):
                my_box = my_boxes[b_i]
                if status[my_box] or my_box in my_keys:  # already open
                    my_boxes.pop(b_i)
                    my_boxes.extend(containedBoxes[my_box])
                    candy_count += candies[my_box]
                    my_keys.extend(keys[my_box])
                    opened_new = True
            if not opened_new:
                return candy_count

        return candy_count
