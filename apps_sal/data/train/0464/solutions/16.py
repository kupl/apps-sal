# [1, 3, 5, 7, ...]

# [1, 3, 5, 7, 9] -> 5 will be the mid point

# if n is odd ->
#   for i->n/2
#       steps += 2**i

# We have to take advante of the symmetry

# if n is even
# [1, 3, 5, 7] -> Mid point is 4
#

# [1,3,5,7,9.11]
class Solution:
    def minOperations(self, n: int) -> int:
        mid_point = (2 * (n // 2)) + 1 - (n % 2 == 0)
        return sum([mid_point - ((2 * i) + 1) for i in range(n // 2)])
