class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        boxes = set(initialBoxes)
        bfs = [i for i in initialBoxes if status[i]]
        for i in bfs:
            for j in containedBoxes[i]:
                boxes.add(j)
                if status[j]:
                    bfs.append(j)
            for j in keys[i]:
                if j in boxes and status[j]==0:
                    bfs.append(j)
                status[j] = 1
        return sum(candies[i] for i in bfs)

