class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Corner cases
        if k > n:
            return 0

        # We will use 4 pointers: p1, p2, p3, p4
        # p1 will initially start at -1. It will always point to the \"previous\" odd number
        # that we DONT want to include the in the current count
        # p2 will point to the first odd number that we want to count
        # p3 will point the the kth odd number starting from p2's odd number
        # p4 will point to the next odd number after p3 if it exists, else will point to n
        # Given p1, p2, p3, p4, the number of nice subarrays in this window equals (p2-p1)*(p4-p3)
        # After that, we set p1 to p2, p3 to p4. Then move p4 (if you can) to the next odd number, and move
        # p2 to the next odd number. Do this until you can't move p4 anymore.
        ans = 0
        p1 = p2 = p3 = p4 = -1
        while p4 < n:
            # Move p2 to the next odd number
            p2 += 1
            while p2 < n and nums[p2] % 2 == 0:
                p2 += 1
                if p2 == n:
                    return ans
            # p2 now points to the 1st odd number
            # Now move p3 to the kth odd number (Note that for k=1 p3 coincides with p2)
            # For the first time the loop is executed, we find the k-th 1 by moving forward one index at a time.
            # For the second loop onward, we simply set p3 to p4. Also note that because we entered the loop,
            # p4 < n, hence p4 must point to a 1, hence we can simply set p3 to p4.
            if p4 == -1:
                p3 = p2
                remaining = k - 1
                while p3 < n and remaining:
                    p3 += 1
                    if p3 == n:
                        return ans
                    if nums[p3] % 2 == 1:
                        remaining -= 1
            else:
                p3 = p4
            # p3 now points to the kth odd number
            # Now move p4 to the next odd number
            p4 = p3 + 1  # p3 is at most n-1, because we would have returned otherwise.
            while p4 < n:
                if nums[p4] % 2 == 1:
                    break
                p4 += 1
            # p4 is now either n or the next odd number after p3
            # Now compute the number of nice subarrays in this window and add to ans
            ans += (p2 - p1) * (p4 - p3)
            # To set up for the next round, set p1 to p2
            p1 = p2
        return ans
