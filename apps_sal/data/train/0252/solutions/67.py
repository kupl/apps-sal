class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        hp = []
        
        for i, r in enumerate(ranges):
            if r != 0:
                heapq.heappush(hp, (max(i-r, 0), -(i+r)))
        #1-5,-2-6, 3-7, 4-8
        ans = []
        while hp:
            start, end = heapq.heappop(hp)
            end = -end
            if not ans:
                ans.append((start, end))
            else:
                #Not overlapped
                if start > ans[-1][1]:
                    return -1
                
                #Already covered
                if end <= ans[-1][1]:
                    continue

                if len(ans) >= 2 and start <= ans[-2][1]:
                    ans[-1] = (start, end)
                elif start <= ans[-1][1]:
                    ans.append((start, end))
                #print(\"here\")
                #print(ans)
            if ans and ans[-1][1] >= n:
                break
        
        print(ans)
        return len(ans) if ans and ans[-1][1] >= n else -1

