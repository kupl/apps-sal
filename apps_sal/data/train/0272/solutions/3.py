class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        stack = deque(initialBoxes)
        seen = set()        
        kseen = set()
        while stack:
            for _ in range(len(stack)):
                box = stack.popleft()
                seen.add(box)
                for key in keys[box]:
                    status[key] = 1
                for tbox in containedBoxes[box]:
                    if tbox not in seen:
                        stack.append(tbox)
        res = 0
        for box in seen:
            if candies[box] and status[box]:
                res += candies[box]
        return res
