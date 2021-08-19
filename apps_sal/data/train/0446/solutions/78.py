class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        print(c)
        cnt, remaining = Counter(c.values()), len(c)
        print(cnt)

        for key in range(1, len(arr) + 1):
            print(cnt[key], key)
            if k >= key * cnt[key]:
                k -= key * cnt[key]
                remaining -= cnt[key]
            else:
                #print('In Else during key',key)
                return remaining - k // key
                #print('After Return',key)
        return remaining
