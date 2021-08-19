class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        (OPEN, CLOSED) = (1, 0)
        q = deque(initialBoxes)
        keys_obtained = set((i for i in range(len(status)) if status[i] == OPEN))
        count = 0
        while set(q) & keys_obtained:
            q2 = deque()
            while q:
                box = q.popleft()
                if box in keys_obtained:
                    count += candies[box]
                    keys_obtained |= set(keys[box])
                    q.extend(containedBoxes[box])
                else:
                    q2.append(box)
            q = q2
        return count
