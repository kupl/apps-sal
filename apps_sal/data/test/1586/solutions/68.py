n = int(input())
if n % 2 != 0:
    print((0))
    return
n //= 10


def Base_10_to_n(X, n):
    X_dumy = X
    out = ''
    while X_dumy > 0:
        out = str(X_dumy % n) + out
        X_dumy = X_dumy // n
    return out


n = Base_10_to_n(n, 5)
n = reversed(list(n))
tmp = 1
ans = 0

for i in n:
    ans += int(i) * tmp
    tmp = tmp * 5 + 1
print(ans)
