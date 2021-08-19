class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # L, C = len(arr), collections.Counter(arr)
        # S = sorted(C.values(), reverse = True)
        # T = itertools.accumulate(S)
        # for i,v in enumerate(T):
        #     if v >= len(arr)//2: return i + 1

        h = [(val * (-1), key) for key, val in list(Counter(arr).items())]
        heapify(h)
        # print(h)
        num_int = 0
        count = 0
        while 2 * count * (-1) < len(arr):
            c, i = heappop(h)
            count += c
            num_int += 1
            # print(seen)
        return num_int
