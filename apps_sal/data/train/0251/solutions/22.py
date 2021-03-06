"""
1006. Clumsy Factorial.  Medium

Normally, the factorial of a positive integer n is the product
of all positive integers less than or equal to n.
For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.

We instead make a clumsy factorial: using the integers in decreasing order,
we swap out the multiply operations for a fixed rotation of operations:
multiply (*), divide (/), add (+) and subtract (-) in this order.

For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.
However, these operations are still applied using the usual order
of operations of arithmetic: we do all multiplication and division
steps before any addition or subtraction steps, and multiplication
and division steps are processed left to right.

Additionally, the division that we use is floor division
such that 10 * 9 / 8 equals 11.  This guarantees the result is an integer.

Implement the clumsy function as defined above: given an integer N,
it returns the clumsy factorial of N.

Example 1:
Input: 4
Output: 7
Explanation: 7 = 4 * 3 / 2 + 1

Example 2:
Input: 10
Output: 12
Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1

Note:
1 <= N <= 10000
-2^31 <= answer <= 2^31 - 1  
The answer is guaranteed to fit within a 32-bit integer.

Accepted 11, 010 / 20, 603 submissions.
"""


class SolutionWhile:
    """
    Runtime: 36 ms, faster than 77.40% of Python3 online submissions for Clumsy Factorial.
    Memory Usage: 14.2 MB, less than 41.24% of Python3 online submissions for Clumsy Factorial.

    Runtime: 40 ms, faster than 68.26% in Python3.
    Memory Usage: 12.8 MB, less than 100.00% in Python3.
    """

    def clumsy(self, N: int) -> int:
        """
        1006. Clumsy Factorial
        """
        R = N
        N -= 1
        if N:
            R *= N
            N -= 1
            if N:
                R //= N
                N -= 1
                if N:
                    R += N
                    N -= 1
        while N:
            if N > 2:
                R -= N * (N - 1) // (N - 2)
                N -= 3
            elif N > 1:
                R -= N * (N - 1)
                N -= 2
            elif N > 0:
                R -= N
                N -= 1
            if not N:
                break
            R += N
            N -= 1
        return R


class Solution:
    pass


Solution = SolutionWhile
