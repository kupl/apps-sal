class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        acc=[]
        temp=0
        for u in arr:
            temp+=u%2
            acc.append(temp%2)
        L=len(arr)
        ones=sum([u%2 for u in acc])
        return ones*(L-ones+1)%(10**9+7)

