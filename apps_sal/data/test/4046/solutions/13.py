n = int(input())
a = list(map(int, input().split()))
p = [0] * n
for i in range(n - 2, -1, -1):
    p[i] = p[i + 1] - a[i]
w = max(p)
w = n - w
for i in range(len(p)):
    p[i] += w
if list(sorted(p)) == [i for i in range(1, n + 1)]:
    print(*p)
else:
    print(-1)
