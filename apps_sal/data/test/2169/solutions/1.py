(h, w, d) = map(int, input().split())
a = [0] * h
for i in range(h):
    a[i] = list(map(int, input().split()))
num = [[] for i in range(w * h + 1)]
for i in range(h):
    for j in range(w):
        num[a[i][j]].append([i, j])
s = [0] * (h * w + 1)
for i in range(1, h * w - d + 1):
    s[d + i] = s[i] + abs(num[d + i][0][0] - num[i][0][0]) + abs(num[d + i][0][1] - num[i][0][1])
q = int(input())
for i in range(q):
    (L, R) = map(int, input().split())
    print(s[R] - s[L])
