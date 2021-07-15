class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        c = collections.Counter()
        for i in arr:
            c[i%k] += 1
        return all((i == 0 and c[i]%2 == 0) or (i != 0 and c[i] == c[k-i]) for i in c)
