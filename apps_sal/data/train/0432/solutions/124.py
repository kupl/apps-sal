class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        freq = Counter(nums)
        start = []
        for (n, v) in freq.items():
            if freq[n - 1] == 0:
                start.append(n)
        while start:
            num = start.pop()
            if freq[num] == 0:
                continue
            else:
                for t in range(num + k - 1, num - 1, -1):
                    if freq[t] < freq[num]:
                        return False
                    freq[t] -= freq[num]
                    if freq[t] == 0 and freq[t + 1] > 0:
                        start.append(t + 1)
        return True
