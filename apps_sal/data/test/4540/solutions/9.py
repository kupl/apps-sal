n = int(input())
a = list(map(int, input().split()))
a = [0] + a + [0]
tnp = 0
for i in range(1, n + 2):
    tnp += abs(a[i] - a[i - 1])
for i in range(n):
    ans = tnp - abs(a[i + 1] - a[i]) - abs(a[i + 2] - a[i + 1]) + abs(a[i + 2] - a[i])
    print(ans)
