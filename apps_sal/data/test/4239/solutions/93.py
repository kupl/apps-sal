# 6**6 < 10**5 < 6**7
# 9**5 < 10**5 < 9**6

def solve(n):
    if n < 6:
        return n
    elif n < 9:
        return n - 5
    else:
        now_6 = 6
        while now_6 * 6 <= n:
            now_6 *= 6

        now_9 = 9
        while now_9 * 9 <= n:
            now_9 *= 9

        ans = float('inf')
        for i in range(n // now_6 + 1):
            cnt = i + (n - now_6 * i) // now_9 + solve((n - now_6 * i) % now_9)
            if cnt < ans:
                ans = cnt

        return ans


print(solve(int(input())))
