class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        locked_boxes = set()
        unused_keys = set()
        candy_count = 0
        cur_box = []
        for box in initialBoxes:
            if status[box] or box in unused_keys:
                candy_count += candies[box]
                for i in keys[box]:
                    if not status[i]:
                        if i not in locked_boxes:
                            unused_keys.add(i)
                        else:
                            locked_boxes.remove(i)
                            cur_box.append(i)
                for i in containedBoxes[box]:
                    if not status[i] and i not in unused_keys:
                        locked_boxes.add(i)
                    else:
                        cur_box.append(i)
                        if i in unused_keys:
                            unused_keys.remove(i)
                if box in unused_keys:
                    unused_keys.remove(box)
            else:
                locked_boxes.add(box)
        while cur_box:
            box = cur_box.pop()
            candy_count += candies[box]
            for i in keys[box]:
                if not status[i]:
                    if i not in locked_boxes:
                        unused_keys.add(i)
                    else:
                        locked_boxes.remove(i)
                        cur_box.append(i)
            for i in containedBoxes[box]:
                if not status[i] and i not in unused_keys:
                    locked_boxes.add(i)
                else:
                    cur_box.append(i)
                    if i in unused_keys:
                        unused_keys.remove(i)
            if box in unused_keys:
                unused_keys.remove(box)
        return candy_count
