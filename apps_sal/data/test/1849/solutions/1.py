import sys

q = 998244353


def exp(b, e):
    ans = 1
    while e > 0:
        if e % 2 == 0:
            e = e // 2
            b = (b * b) % q
        else:
            ans = ans * b
            e = e - 1
    return ans


n = int(sys.stdin.readline().strip())
x = []
for i in range(1, n):
    ans = 0
    ans = ans + 9 * exp(10, n - i - 1)
    ans = ans + 9 * exp(10, n - i - 1)
    ans = ans + (n - i - 1) * 81 * exp(10, n - i - 2)
    ans = ans * 10
    ans = ans % q
    x.append(str(ans))
x.append(str(10))
print(" ".join(x))
