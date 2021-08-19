class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # One very important lesson to learn from this problem: if asking for subsequences, see if
        # the problem requires some kind of ordering. If not, then you can safely sort the array!
        # Any subset of A is a subsequence (if you put it back into the original order).
        # This problem then becomes trivial. Sort nums, then for each A[i] find the maximum A[j]
        # s.t. A[i] + A[j] <= target. Once you've found A[j], notice that every element in [i + 1, j]
        # can be turned on or off, so that's 2^(j - i) subsequences (notice we cannot turn off A[i] because
        # we are counting \"all subsequences whose min element is A[i]\"). How do we prove this counts
        # every valid subsequence? Because every valid subsequence has a min element, and we consider
        # every A[i] as the min element. So as long as our logic for finding \"number of subsequences whose
        # min element is A[i]\" is correct, we should count all valid subsequences.
        nums.sort()
        ret, l, r = 0, 0, len(nums) - 1

        p, pw = [], 1
        for d in range(len(nums)):
            p.append(pw)
            pw <<= 1

        while l <= r:
            if nums[l] + nums[r] <= target:
                ret = (ret + p[r - l]) % (10**9 + 7)  # count all subsequences whose min element is nums[l]
                l += 1                                    # we never have to consider nums[l] as the min element again
            else:
                r -= 1
        return ret
