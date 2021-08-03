h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

b = []

ans = [[0] * w] * h

for i in range(n):
    b += [i + 1] * a[i]

for i in range(h):
    if i % 2 == 0:
        ans[i] = b[i * w: (i + 1) * w]
    else:
        ans[i] = reversed(b[i * w: (i + 1) * w])

for i in range(h):
    print(*ans[i])
