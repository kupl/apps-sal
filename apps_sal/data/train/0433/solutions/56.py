class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        start = 0
        s = 0
        count = 0
        for end in range(len(arr)):
            s = s + arr[end]
            if end - start + 1 == k:
                if s / k >= threshold:
                    count += 1
                s -= arr[start]
                start += 1
        return count
