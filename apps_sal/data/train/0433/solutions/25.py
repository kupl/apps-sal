class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Sliding window problem

        # Edge case
        if len(arr) < k:
            return None

        # Initialize variables and this is required to initilize the first condition as in the while loop
        # k_sum = k_sum - arr[p1] + arr[p2] already take to next k+1 calculation
        k_sum = sum([arr[i] for i in range(0, k)])
        count = 0
        p1, p2 = 0, k

        if k_sum / k >= threshold:
            count += 1

        while p2 < len(arr):

            k_sum = k_sum - arr[p1] + arr[p2]

            if k_sum / k >= threshold:
                count += 1

            p1 += 1
            p2 += 1

        return count


#         ## Backtacking time out!
#         res = []

#         def helper(start_pos = 0, curr_arr = []):
#             if len(curr_arr) == k and mean(curr_arr) >= threshold:
#                 res.append(curr_arr[:])
#             elif len(curr_arr) == k:
#                 return
#             else:
#                 curr_arr.append(arr[start_pos])

#                 helper(start_pos = start_pos + 1, curr_arr = curr_arr)

#                 curr_arr.pop()


#         for i in range(len(arr) - k + 1):
#             helper(start_pos = i, curr_arr = [])

#         return len(res)
