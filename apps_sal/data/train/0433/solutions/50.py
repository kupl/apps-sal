class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold*=k
        n = len(arr)
        l=0
        tmp_sum=0
        count=0
        for i in range(k):
            tmp_sum+=arr[i]
        if tmp_sum>=threshold:
            count+=1
        for l in range(n-k):
            tmp_sum-=arr[l]
            r=l+k
            tmp_sum+=arr[r]
            if tmp_sum>=threshold:
                count+=1
        return count

