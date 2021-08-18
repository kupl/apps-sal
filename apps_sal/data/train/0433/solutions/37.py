class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i = 0
        j = i + k
        s = sum(arr[i:j])
        c = 0
        while(j <= len(arr)):
            if(s // k >= threshold):
                c += 1
            s -= arr[i]
            if(j < len(arr)):
                s += arr[j]
            j += 1
            i += 1
        return c
