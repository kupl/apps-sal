(N, A, B) = list(map(int, input().split()))
V = list(map(int, input().split()))
V.sort(reverse=True)
total = sum(V[:A])
ave = total / A
tmp = V[A - 1]
count = V.count(tmp)


def combination(n, r):
    if n - r > r:
        r = n - r
    tmp = 1
    for i in range(n - r + 1, n + 1):
        tmp *= i
    for i in range(1, r + 1):
        tmp //= i
    return tmp


if V[0] == V[A - 1]:
    ans = 0
    for i in range(A, min(B, count) + 1):
        ans += combination(count, i)
else:
    count2 = V[:A].count(tmp)
    ans = combination(count, count2)
print(ave)
print(ans)
