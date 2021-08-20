(A, B) = map(int, input().split())


def f(x):
    if x % 2 == 0:
        if x // 2 % 2 == 0:
            ans = x
        else:
            ans = 1 ^ x
    else:
        ans = f(x - 1) ^ x
    return ans


ans = f(A - 1) ^ f(B)
print(ans)
