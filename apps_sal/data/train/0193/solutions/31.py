class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        order = collections.Counter(arr).most_common()
        ans = 0
        sum = 0
        mid = len(arr)//2 if len(arr)%2==0 else (len(arr)//2 +1)
        for i,j in order:
            sum+=j
            ans+=1
            if sum >= mid:
                break
        return ans  

