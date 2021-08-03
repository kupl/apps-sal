class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = {}
        for num in arr:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        heap = []

        for num in list(counter.keys()):
            heapq.heappush(heap, (-counter[num], num))

        n = len(arr)
        i = 0
        cumSum = 0
        while i < n and cumSum < n // 2:
            freq, num = heapq.heappop(heap)
            cumSum += abs(freq)
            i += 1

        return i
