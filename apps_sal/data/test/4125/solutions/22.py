import fractions


def gcdlist(a):
    ans = a[0]
    for i in range(1, len(a)):
        ans = fractions.gcd(ans, a[i])
    return ans


n, y = list(map(int, input().split()))
x = list(map(int, input().split()))
x.append(y)
if y == 1:
    print((abs(x[0] - 1)))
    return

l = []
for i in range(n):
    l.append(abs(x[i + 1] - x[i]))
print((gcdlist(l)))
