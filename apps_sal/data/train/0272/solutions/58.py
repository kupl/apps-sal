class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q = collections.deque()
        for box in initialBoxes:
            q.append(box)
        keys_found = set()
        ans = 0
        found = True
        while q and found:
            size = len(q)
            found = False
            for _ in range(size):
                cur = q.popleft()
                if status[cur] == 0 and cur not in keys_found:
                    q.append(cur)
                else:
                    found = True
                    ans += candies[cur]
                    for box in containedBoxes[cur]:
                        q.append(box)
                    for key in keys[cur]:
                        keys_found.add(key)
        return ans
