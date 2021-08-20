class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        hold = initialBoxes
        res = 0
        key = set()
        flag = True
        while flag:
            nxt = []
            flag = False
            for i in range(len(hold)):
                cur = hold.pop()
                if status[cur] == 1 or (status[cur] == 0 and cur in key):
                    flag = True
                    res += candies[cur]
                    for k in keys[cur]:
                        key.add(k)
                    for b in containedBoxes[cur]:
                        nxt.append(b)
                else:
                    nxt.append(cur)
            hold = nxt
        return res
