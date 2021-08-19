class Heap:

    def __init__(self, initial=None, key=lambda x: x):
        self.key = key
        if initial:
            self._data = [(key(item), item) for item in initial]
            heapq.heapify(self._data)
        else:
            self._data = []

    def push(self, item):
        heapq.heappush(self._data, (self.key(item), item))

    def pop(self):
        return heapq.heappop(self._data)[1]

    def peek(self):
        return self._data[0][1]


class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        powers = {}
        heap = Heap(key=lambda n: -self._get_power(n, powers))
        for n in range(lo, lo + k):
            heap.push(n)
        for n in range(lo + k, hi + 1):
            heap.push(n)
            heap.pop()
        return heap.peek()

    def _get_power(self, n: int, powers: dict) -> int:
        orig_n = n
        if n not in powers:
            power = 0
            while n != 1:
                if n % 2:
                    n = n * 3 + 1
                else:
                    n //= 2
                power += 1
                if n in powers:
                    power += powers[n]
                    break
            powers[orig_n] = power
        return powers[orig_n] - 1 / orig_n
