N = int(input())
A = list(map(int, input().split()))
ans = 0


def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    while y > 0:
        temp = x % y
        x = y
        y = temp
    return x


L = [0]
R = 0

for i in range(N - 1):
    L.append(gcd(A[i], L[i]))
for i in range(N):
    temp = gcd(L[N - i - 1], R)
    R = gcd(R, A[N - i - 1])
    if ans < temp:
        ans = temp

print(ans)
