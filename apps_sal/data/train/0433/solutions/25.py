class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return None
        k_sum = sum([arr[i] for i in range(0, k)])
        count = 0
        (p1, p2) = (0, k)
        if k_sum / k >= threshold:
            count += 1
        while p2 < len(arr):
            k_sum = k_sum - arr[p1] + arr[p2]
            if k_sum / k >= threshold:
                count += 1
            p1 += 1
            p2 += 1
        return count
