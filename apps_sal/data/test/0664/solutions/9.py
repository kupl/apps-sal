n = int(input())
a = list(map(int, input().split()))
sub = []
for i in range(1, n):
    x = a[i] - a[i - 1]
    sub.append(x)
sub.append(a[0] - a[-1])
c = 0
for i in range(n):
    if sub[i] < 0:
        c += 1
        pos = i
if c == 0:
    print(0)
elif c > 1:
    print(-1)
else:
    print(n - pos - 1)
