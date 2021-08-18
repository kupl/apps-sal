n = input()
n = int(n)
md = 998244353
L = list(map(int, input().split()))


def inv(x):
    nonlocal md
    return pow(x, md - 2, md)


ml = 1
ans = 0
for el in reversed(L):
    ml *= 100
    ml *= inv(el)
    ml %= md
    ans += ml
    ans %= md
print(ans)
