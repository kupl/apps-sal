class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = collections.defaultdict(int)
        for num in arr:
            d[num%k]+=1
        print(d)
        for i in range(k):
            if i in d:
                if i!=k-i and k-i in d and d[i] ==d[k-i]:
                    continue
                elif (i == 0 or i==k-i) and d[i]%2 == 0:
                    continue

                else:
                    return False
        return True
