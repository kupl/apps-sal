from collections import deque


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        # Step 1: Traverse through intialBoxes using it sort of as our stack
        # With each box, add candies to result, open every box we have a key for, add every contained box onto stack
        # use array to keep track of seen boxes

        # what to do about keys? could have box that isn't opened but will be opened later on
        # possible soln: skip that box, come back to it later on, if we reach a point where every box on stack can't be opened we end

        n = len(status)
        seen, queue, result = [False] * n, deque(initialBoxes), 0
        num_locked = 0

        for box in initialBoxes:
            seen[box] = True

        while queue:
            box = queue.popleft()

            # Check if we can process box yet.
            if not status[box]:
                queue.append(box)
                num_locked += 1
                if num_locked == len(queue):
                    break
                continue

            num_locked = 0
            result += candies[box]

            # Open every box we have a key for.
            for k in keys[box]:
                status[k] = 1

            # Add all contained boxes to queue.
            for cb in containedBoxes[box]:
                if not seen[cb]:
                    queue.append(cb)
                    seen[cb] = True

        return result
