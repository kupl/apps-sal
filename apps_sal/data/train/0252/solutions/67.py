class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        hp = []

        for i, r in enumerate(ranges):
            if r != 0:
                heapq.heappush(hp, (max(i - r, 0), -(i + r)))
        ans = []
        while hp:
            start, end = heapq.heappop(hp)
            end = -end
            if not ans:
                ans.append((start, end))
            else:
                if start > ans[-1][1]:
                    return -1

                if end <= ans[-1][1]:
                    continue

                if len(ans) >= 2 and start <= ans[-2][1]:
                    ans[-1] = (start, end)
                elif start <= ans[-1][1]:
                    ans.append((start, end))
            if ans and ans[-1][1] >= n:
                break

        print(ans)
        return len(ans) if ans and ans[-1][1] >= n else -1
