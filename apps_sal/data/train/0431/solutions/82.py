class Solution:
    # def sumSubarrayMins(self, A):
    #     n, mod = len(A), 10**9 + 7
    #     left, right, s1, s2 = [0] * n, [0] * n, [], []
    #     for i in range(n):
    #         count = 1
    #         while s1 and s1[-1][0] > A[i]: count += s1.pop()[1]
    #         left[i] = count
    #         s1.append([A[i], count])
    #     for i in range(n)[::-1]:
    #         count = 1
    #         while s2 and s2[-1][0] >= A[i]: count += s2.pop()[1]
    #         right[i] = count
    #         s2.append([A[i], count])
    #     print(left)
    #     print(right)
    #     return sum(a * l * r for a, l, r in zip(A, left, right)) % mod
    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        l_large = [0] * n
        l_stack = [(A[0], 0)] # mono increasing
        r_large = [0] * n
        r_stack = [(A[n-1], n-1)] # mono increasing
        for i in range(1, n):
            while l_stack and A[i] <= l_stack[-1][0]:
                _, idx = l_stack.pop()
                l_large[i] = max(l_large[i], i-idx+l_large[idx])
            else: l_stack.append((A[i], i))     
            while r_stack and A[n-i-1] < r_stack[-1][0]:
                _, idx = r_stack.pop()
                r_large[n-i-1] = max(r_large[n-i-1], idx-(n-i-1)+r_large[idx])
            else: r_stack.append((A[n-i-1], n-i-1))     
        return sum((1+l_large[i] + r_large[i] + l_large[i] * r_large[i])*A[i] for i in range(n)) % int(1000000007)
