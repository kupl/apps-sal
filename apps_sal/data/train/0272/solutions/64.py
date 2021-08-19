class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        done = set()
        to_open = set()
        current_keys = set()
        opened = list()
        for box in initialBoxes:
            if status[box] == 1:
                opened.append(box)
            else:
                to_open.add(box)
        total = 0
        while opened:
            box = opened.pop()
            if box in done:
                continue
            total += candies[box]
            done.add(box)
            for openable in keys[box]:
                if openable in to_open:
                    opened.append(openable)
                    to_open.remove(openable)
                else:
                    current_keys.add(openable)
            for contained in containedBoxes[box]:
                if status[contained] == 1:
                    opened.append(contained)
                elif contained in current_keys:
                    opened.append(contained)
                    current_keys.remove(contained)
                else:
                    to_open.add(contained)
        return total
