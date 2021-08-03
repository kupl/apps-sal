n = int(input())
A = list(map(int, input().split()))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


l = [A[0]] * n
r = [A[-1]] * n
for i in range(n - 1):
    l[i + 1] = gcd(l[i], A[i + 1])
    r[-i - 2] = gcd(r[-i - 1], A[-i - 2])

ans = 0
for i in range(n):
    if i == 0:
        ans = max(ans, r[1])
        continue
    if i == n - 1:
        ans = max(ans, l[-2])
        continue
    ans = max(ans, gcd(l[i - 1], r[i + 1]))
print(ans)
