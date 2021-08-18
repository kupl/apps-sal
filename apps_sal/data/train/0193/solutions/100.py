class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        h = [(val * (-1), key) for key, val in list(Counter(arr).items())]
        heapify(h)
        num_int = 0
        count = 0
        while 2 * count * (-1) < len(arr):
            c, i = heappop(h)
            count += c
            num_int += 1
        return num_int
