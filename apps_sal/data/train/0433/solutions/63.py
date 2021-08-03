class Solution:
    def numOfSubarrays(self, arr, k, threshold) -> int:
        s = 0
        sub = arr[0:k]
        subSum = sum(sub)
        avg = subSum / k
        if avg >= threshold:
            s += 1
        i = k
        j = 0
        while i < len(arr):
            subSum += arr[i]
            subSum -= arr[j]
            j += 1
            i += 1
            avg = subSum / k
            if avg >= threshold:
                s += 1
        return s
