from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        temp = sorted(list(cnt.keys()), key = lambda x: cnt[x])
        curr = 0
        for i in range(1, len(temp)+1):
            curr += cnt[temp[-i]]
            if curr >= len(arr)/2:
                return i

