class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        currkeys, ret, taken = set(), 0, [0] * len(status)
        q = collections.deque(initialBoxes)
        while q:
            l = len(q)
            opened = False
            for _ in range(l):
                curr = q.popleft()
                taken[curr] = 1
                if curr not in currkeys and status[curr] == 0:
                    q.append(curr)
                else:
                    opened = True
                    ret += candies[curr]
                    if keys[curr]: currkeys |= set([key for key in keys[curr]])
                    for b in containedBoxes[curr]:
                        if not taken[b]: q.append(b)
            if not opened: break
        return ret

