class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        if not initialBoxes:
            return 0
        unused_keys = set()
        boxes = set([i for i in initialBoxes if status[i] == 0])
        
        Q = collections.deque([i for i in initialBoxes if status[i] == 1])
        res = 0
        while Q:
            cur = Q.popleft()
            res += candies[cur]
            for k in keys[cur]:
                if k in boxes:
                    Q.append(k)
                    boxes.discard(k)
                else:
                    unused_keys.add(k)
            for b in containedBoxes[cur]:
                if b in unused_keys or status[b] == 1:
                    Q.append(b)
                    unused_keys.discard(b)
                else:
                    boxes.add(b)
        return res
