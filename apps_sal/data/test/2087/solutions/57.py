A, B, C = map(int, input().split())

def func(x):
    return x * (x + 1) // 2
mod = 998244353
ans = func(A) * func(B) * func(C) % mod
print(ans)
