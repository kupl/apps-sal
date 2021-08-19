class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q = collections.deque()
        keys_set = set()
        boxes_set = set()
        for box in initialBoxes:
            if status[box] == 1 or box in keys_set:
                q.append(box)
                for key in keys[box]:
                    keys_set.add(key)
                    if key in boxes_set:
                        q.append(key)
                        boxes_set.remove(key)
            else:
                boxes_set.add(box)
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
                if status[nei] == 1 or nei in keys_set:
                    q.append(nei)
                    for key in keys[nei]:
                        keys_set.add(key)
                        if key in boxes_set:
                            q.append(key)
                            boxes_set.remove(key)
                else:
                    boxes_set.add(nei)
        return res
