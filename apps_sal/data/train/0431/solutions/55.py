class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        mod = 10**9 + 7
        curr_sum = 0
        last_sum = 0
        stack = []

        for a in A:
            cnt = 1
            last_sum = (last_sum + a) % mod
            while stack and a < stack[-1][0]:
                b, c = stack.pop()
                cnt = (cnt + c) % mod
                last_sum = (last_sum - (b - a) * c) % mod

            if stack and stack[-1][0] == a:
                stack[-1][1] = (stack[-1][1] + cnt) % mod
            else:
                stack.append([a, cnt])

            curr_sum = (curr_sum + last_sum) % mod

        return curr_sum
