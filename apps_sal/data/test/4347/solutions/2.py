def cal(k):
    ans = 1
    for i in range(k + 1, 2 * k):
        ans *= i
    for i in range(1, k):
        ans //= i
    t = 1
    for i in range(1, k):
        t *= i
    ans *= t * t
    return ans


print(cal(int(input()) // 2))
