class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        target = threshold * k
        n_subarrays = n - k + 1

        curr_sum = sum(arr[0:k])
        count = 0 if (curr_sum < target) else 1

        for i in range(1, n_subarrays):
            curr_sum += (-arr[i - 1] + arr[i + k - 1])
            count = count if (curr_sum < target) else (count + 1)

        return count
