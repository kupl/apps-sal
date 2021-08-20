N = int(input())
s = input()
t = input()
mod = 10 ** 9 + 7
cur = 0
ans = 1
for (i, (x, y)) in enumerate(zip(s, t)):
    if cur == 1:
        cur = 2
        continue
    if x == y:
        if i == 0:
            ans = 3
        elif cur == 0:
            ans *= 2 % mod
        else:
            cur = 0
            continue
    elif i == 0:
        ans *= 6
        cur = 1
    elif cur == 0:
        ans *= 2
        ans %= mod
        cur = 1
    else:
        ans *= 3 % mod
        cur = 1
print(ans % mod)
