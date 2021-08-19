class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q = collections.deque()
        keys_set = set([i for i in range(len(status)) if status[i] == 1])
        boxes_set = set(initialBoxes[:])
        for box in initialBoxes:
            if box in keys_set:
                q.append(box)
        res = 0
        visited = set()
        while q:
            boxi = q.popleft()
            if boxi in visited:
                continue
            else:
                visited.add(boxi)
                res += candies[boxi]
            for nei in containedBoxes[boxi]:
                if nei in keys_set:
                    q.append(nei)
                boxes_set.add(nei)
            for key in keys[boxi]:
                if key in boxes_set and key not in keys_set:
                    q.append(key)
                keys_set.add(key)
        return res
