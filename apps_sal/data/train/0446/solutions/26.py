class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = defaultdict(int)
        for num in arr:
            freq[num] += 1
        freq_arr = []
        for t, v in freq.items():
            freq_arr.append([v, t])
        freq_arr.sort(reverse=True)
        while k > 0:
            amount, rem = freq_arr.pop()
            if amount <= k:
                del freq[rem]
                k -= amount
            else:
                freq[rem] = amount - k
                k = 0
        return len(freq)
