class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        curr = 0
        left = len(bloomDay) * [0]
        right = len(bloomDay) * [0]
        days = defaultdict(list)
        for i in range(len(bloomDay)):
            days[bloomDay[i]].append(i)
        sorted_days = sorted(days)
        for i in sorted_days:
            for x in days[i]:
                right[x] = 1
                left[x] = 1
                if x < len(bloomDay) - 1:
                    right[x] += right[x + 1]
                if x > 0:
                    left[x] += left[x - 1]
                if (left[x] - 1) % k + (right[x] - 1) % k + 1 >= k:
                    curr += 1
                    if curr == m:
                        return i
                right[x - left[x] + 1] = left[x] + right[x] - 1
                left[x + right[x] - 1] = left[x] + right[x] - 1
        return -1
