class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        heap = []
        self.memo = {}
        for i in range(lo, hi + 1):
            power = self.computer_power(i)
            self.memo[i] = power
            heapq.heappush(heap, (power, i))
        k_now = 1
        while heap:
            (new_power, i) = heapq.heappop(heap)
            if k_now == k:
                return i
            k_now += 1
        return result

    def computer_power(self, val):
        if val == 1:
            return 0
        if val in self.memo:
            return self.memo[val]
        if val % 2 == 0:
            return 1 + self.computer_power(val // 2)
        else:
            return 1 + self.computer_power(3 * val + 1)
