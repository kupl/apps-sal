class Solution:
    def getProbability(self, balls: List[int]) -> float:

        total = sum(balls)

        def factorial(n):
            if n == 0:
                return 1
            if n < 3:
                return n
            return n * factorial(n - 1)

        self.match = 0
        self.total = 0

        def helper(p, left1, left2, cnt1, cnt2, per1, per2):
            if left1 == 0 and left2 == 0:
                self.total += per1 * per2
                self.match += per1 * per2 * (cnt1 == cnt2)
            elif left1 >= 0 and left2 >= 0:
                for k in range(balls[p] + 1):
                    helper(p + 1, left1 - k, left2 - balls[p] + k, cnt1 + (k > 0), cnt2 + (balls[p] - k > 0), per1 / factorial(k), per2 / factorial(balls[p] - k))

        helper(0, total // 2, total // 2, 0, 0, factorial(total // 2), factorial(total // 2))
        # print(self.match)
        # print(self.total)
        return self.match / self.total


#         Track how many balls are left to fill each box as cnt1 and cnt2.
# Count different colors in each box as col1 and col2; compare in the end.
# The initial/maximum number of permutatons in each box is (n / 2)!
# When selecting m balls of particular color, we reduce the number of permutations by m! if the color is the same, no difference, just like [1, 1 / 2, 3] and [1, 1 / 2, 3]. Even we change the position of the two 1, it makes no difference. However, the order of 2, and 3 matters.
# When both cnt1 and cnt2 are zero, prm1 and prm2 are permutations in each box.
# - Number of permutations = (n / 2)! / (m1! * m2! * ... * mk!).
# - The total number of permutations with two boxes is prm1 * prm2.


#         total = sum(balls)
#         k = len(balls)

#         def theSame(added):
#             res = 0
#             for i in range(k):
#                 if added[i] == 0:
#                     res -= 1
#                 elif balls[i] == added[i]:
#                     res += 1
#             return res == 0


#         def combination(this, pick):
#             pick = min(this-pick, pick)
#             res = 1
#             i = this
#             j = 1
#             while i > pick:
#                 res *= i
#                 res /= j
#                 i -= 1
#                 j += 1
#             return res

#         def helper(i, added, cur):

#             if cur == total // 2:

#                 if theSame(added):
#                     res = 1
#                     for i in range(k):
#                         res *= combination(balls[i], added[i])
#                     return res
#                 return 0
#             if i == k:
#                 return 0
#             if cur > total // 2:
#                 return 0
#             res = 0
#             for t in range(balls[i]+1):
#                 added[i] = t
#                 res += helper(i+1, added, cur+t)
#             added[i] = 0
#             return res

#         added = [0] * k
#         return helper(0, added, 0) / combination(total, total // 2)
