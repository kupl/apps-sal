class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        s = s + ' '
        out = 0
        deleted = set()
        start = 0
        l = len(s)
        while True:
            prev = '='
            to_delete = []
            for i in range(start, l):
                if i in deleted:
                    continue
                if s[i] == prev:
                    to_delete.append((cost[prev_i], prev_i))
                elif to_delete:
                    to_delete.append((cost[prev_i], prev_i))
                    break
                prev = s[i]
                prev_i = i
            else:
                break
            start = prev_i
            
            to_delete.sort(reverse=True)
            for i in range(1, len(to_delete)):
                out += to_delete[i][0]
                deleted.add(to_delete[i][1])
        return out
            
            
        

