class Solution:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        boxes = set(initialBoxes)
        bfs = [i for i in boxes if status[i]]
        for i in bfs:
            for j in containedBoxes[i]:
                boxes.add(j)
                if status[j]:
                    bfs.append(j)
            for j in keys[i]:
                if status[j] == 0 and j in boxes:
                    bfs.append(j)
                status[j] = 1
        return sum(candies[i] for i in bfs)

