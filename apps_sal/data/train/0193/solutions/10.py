from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        h = []
        for num, freq in freq.items():
            print(num, freq)
            heappush(h, (-freq, num))
        count = 0
        ret = 0
        while count < (len(arr) // 2):
            count += -heappop(h)[0]
            ret += 1
        return ret
