from collections import deque
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        cur_queue = deque(initialBoxes)
        next_queue = deque([])
        key_set = set([])
        # opened_set = set([])

        total = 0
        while True:
            temp_queue = cur_queue.copy()
            while temp_queue:
                c = temp_queue.popleft()
                if status[c] == 1 or c in key_set:
                    # opened_set.add(c)
                    key_set = key_set.union(keys[c])
                    total += candies[c]
                    for s in containedBoxes[c]:
                        next_queue.append(s)
                else:
                    next_queue.append(c)

            # print(total, next_queue, cur_queue)
            if cur_queue == next_queue:
                break

            cur_queue = next_queue
            next_queue = deque([])
            
        return total
