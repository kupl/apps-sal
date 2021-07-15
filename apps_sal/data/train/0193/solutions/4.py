class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        N = len(arr)
        target = math.ceil(N/2)
        dic = collections.Counter(arr)
        lst = [(num,cnt) for num,cnt in dic.items()]
        lst.sort(key = lambda x: [-x[1],x[0]])
        
        ans = 0
        count = 0
        for num,cnt in lst:
            count += cnt
            ans += 1
            if count >= target:
                return ans
        return ans
