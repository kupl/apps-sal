class Solution:
    # def splitArraySameAverage(self, A: List[int]) -> bool:
    def splitArraySameAverage(self, A: List[int]) -> bool:

        # A subfunction that see if total k elements sums to target
        # target is the goal, k is the number of elements in set B, i is the index we have traversed through so far
        mem = {}

        def find(target, k, i):
            # if we are down searching for k elements in the array, see if the target is 0 or not. This is a basecase
            if k == 0:
                return target == 0

            # if the to-be selected elements in B (k) + elements we have traversed so far is larger than total length of A
            # even if we choose all elements, we don't have enough elements left, there should be no valid answer.
            if k + i > len(A):
                return False

            if (target, k, i) in mem:
                return mem[(target, k, i)]

            # if we choose the ith element, the target becomes target - A[i] for total sum
            # if we don't choose the ith element, the target doesn't change
            mem[(target - A[i], k - 1, i + 1)] = find(target - A[i], k - 1, i + 1) or find(target, k, i + 1)

            return mem[(target - A[i], k - 1, i + 1)]

        n, s = len(A), sum(A)
    # Note that the smaller set has length j ranging from 1 to n//2+1
    # we iterate for each possible length j of array B from length 1 to length n//2+1
    # if s*j%n, which is the sum of the subset, it should be an integer, so we only proceed to check if s * j % n == 0
    # we check if we can find target sum s*j//n (total sum of j elements that sums to s*j//n)
        return any(find(s * j // n, j, 0) for j in range(1, n // 2 + 1) if s * j % n == 0)
