class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        boxes = set(initialBoxes)
        queue = collections.deque()

        for box in boxes:
            if status[box] == 1:
                queue.append(box)

        ans = 0
        seen = set()

        while queue:
            box = queue.popleft()
            if box not in seen:
                seen.add(box)
                ans += candies[box]
            for i in containedBoxes[box]:
                boxes.add(i)
                if status[i] == 1:
                    queue.append(i)

            for j in keys[box]:
                if status[j] == 0 and j in boxes:
                    queue.append(j)
                status[j] = 1

        return ans
