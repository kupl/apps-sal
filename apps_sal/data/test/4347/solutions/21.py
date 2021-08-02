def fact(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans


a = int(input())
ans = fact(a) // (fact(a // 2) * fact(a // 2))
ans *= fact(a // 2 - 1)
ans *= fact(a // 2 - 1)
print(ans // 2)
