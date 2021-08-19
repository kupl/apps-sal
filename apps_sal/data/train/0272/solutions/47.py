class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        self.count = 0
        queue = collections.deque([i for i in initialBoxes if status[i] == 1])
        boxSet = set(initialBoxes)
        keySet = set((i for i in range(n) if status[i] == 1))
        opened = set()
        while queue:
            l = len(queue)
            for i in range(l):
                cur = queue.popleft()
                self.count += candies[cur]
                opened.add(cur)
                for key in keys[cur]:
                    keySet.add(key)
                    if key not in opened and key in boxSet and (key not in queue):
                        queue.append(key)
                for box in containedBoxes[cur]:
                    boxSet.add(box)
                    if box not in opened and box in keySet and (box not in queue):
                        queue.append(box)
        return self.count
