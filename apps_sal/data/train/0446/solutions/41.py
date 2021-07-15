class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = collections.Counter(arr)
        key = sorted(cnt, key = lambda x: cnt[x])
        n_unique = len(key)
        # print(key)
        for i in range(n_unique):
            # print(key[i])
            k = k-cnt[ key[i] ]
            if k<0:
                return n_unique-i
            elif k == 0:
                return n_unique-i-1
        
        return 0
