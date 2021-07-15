N = int(input())
a, b = [], []
for i in range(N):
    c, d = map(int, input().split())
    a.append(c)
    b.append(d)
a.sort()
b.sort()
if N%2 == 1:
    print(b[N//2] - a[N//2] + 1)
else:
    print((b[N//2]+b[N//2-1]) - (a[N//2]+a[N//2-1]) + 1)
