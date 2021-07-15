class Solution:
    def clumsy(self, N: int) -> int:
        return clumsy(N, 1)
        
        
def clumsy(N: int, sign: int) -> int:
    if N == 1:
        return sign * 1
    if N == 2:
        return sign * 2  # sign * 2 * 1
    if N == 3:
        return sign * 6  # sign * 3 * 2 // 1
    if N == 4:
        return sign * 6 + 1  # sign * 4 * 3 // 2 + 1

    return sign * (N * (N-1) // (N-2)) + (N-3) + clumsy(N-4, -1)


# 10 * 9 // 8 + 7 + (-6 * 5 // 4 + 3) + (-2 * 1)
# 11 + 7 - 7 + 3 - 2 == 12

