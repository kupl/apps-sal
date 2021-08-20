class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        h = []
        for num in arr:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        for (k, v) in list(d.items()):
            h.append((-v, k))
        heapq.heapify(h)
        ans = 0
        count = 0
        while count < len(arr) // 2:
            (v, k) = heapq.heappop(h)
            count -= v
            ans += 1
        return ans
