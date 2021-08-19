class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        (q, res) = (collections.deque(initialBoxes), 0)
        while q:
            l = len(q)
            for _ in range(l):
                (b, changed) = (q.popleft(), False)
                if status[b]:
                    changed = True
                    res += candies[b]
                    q.extend(containedBoxes[b])
                    for i in keys[b]:
                        status[i] = 1
                else:
                    q.append(b)
            if not changed:
                return res
        return res
