h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
s = []
for i in range(n):
    for j in range(a[i]):
        s.append(i + 1)
for i in range(h):
    x = []
    for j in range(w):
        x.append(s[w * i + j])
    if i % 2 == 0:
        print(*x)
    else:
        print(*x[::-1])
