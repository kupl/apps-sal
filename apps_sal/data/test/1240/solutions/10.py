n = int(input())
a = [0] * n
R = 0
L = 0
for i in range(n):
    a[i] = list(map(int, input().split()))
    R += a[i][1]
    L += a[i][0]
m = abs(L - R)
ans = 0
for i in range(n):
    b = abs(L - a[i][0] + a[i][1] - (R - a[i][1] + a[i][0]))
    if b > m:
        ans = i + 1
        m = b
print(ans)
