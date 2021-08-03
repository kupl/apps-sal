class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if len(arr) == m:
            return len(arr)
        days = [0] * len(arr)
        for i, x in enumerate(arr, 1):
            days[x - 1] = i
        deq = collections.deque()

        def insert_deq(val, pop):
            if deq and deq[0] == pop:
                deq.popleft()
            while deq and deq[-1] < val:
                deq.pop()
            deq.append(val)
        latest = -1
        for i, x in enumerate(days):
            insert_deq(x, days[i - m] if i >= m else None)
            if i < m - 1:
                continue
            left = days[i - m] if(i - m >= 0) else float('inf')
            right = days[i + 1] if(i + 1 < len(days)) else float('inf')
            max_day_turn1 = deq[0]
            if left > max_day_turn1 and right > max_day_turn1:
                latest = max(latest, min(left, right) - 1)
        return latest
