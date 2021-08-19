class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        reached = set()
        visited = set()
        q = initialBoxes
        yummy = 0
        while q:
            new_q = []
            for box in q:
                reached.add(box)
                if status[box] and box not in visited:
                    visited.add(box)
                    new_q.extend(containedBoxes[box])
                    new_q.extend((unlockedBox for unlockedBox in keys[box] if unlockedBox in reached))
                    yummy += candies[box]
                    for unlockedBox in keys[box]:
                        status[unlockedBox] = 1
            q = new_q
        return yummy
