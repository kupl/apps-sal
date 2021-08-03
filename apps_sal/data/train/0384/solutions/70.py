class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        # 1.Sort the list. Then for each element, it's the maximum of a subsequence if and only if it's on the rightmost side; on the other hand, if it's the minimum then it's on the leftmost side.
        # 2.For any element A[i], suppose there are left elements on its left side and right elements on its right side. Then in 2^(left) subsequences this element appeared as the maximum element and in 2^(right) subsequences it appeares as the minimum element. So the contribution of this element to the final result would be: (2^(left)-2^(right))*A[i] = [2^i-2^(n-i-1)]*A[i]
        Mod = (1e9) + 7
        n = len(A)
        #twoPower = [1]*n
        # for i in range(1, n):
        #   twoPower[i] = (twoPower[i-1]*2)% Mod

        twoPower = [1]
        while len(twoPower) < n:
            twoPower.append((twoPower[len(twoPower) - 1] * 2) % Mod)

        A.sort()
        ans = 0
        for i, a in enumerate(A):
            left = i
            right = n - i - 1
            ans = (ans + (twoPower[left] - twoPower[right]) * a) % Mod

        return int((ans + Mod) % Mod)
