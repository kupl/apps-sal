c, d = map(int, input().split())
n, m = map(int, input().split())
p = 0
k = int(input())
if m * n <= k:
    print(0)
else:
    a = [0] * (m * n + 1)
    for i in range(k + 1, m * n + 1):
        a[i] = min(a[i - n] + c, a[i - 1] + d)
    print(a[m * n])
