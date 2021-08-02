k, n = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
d = []
for i in range(k - 1):
    c += [a[i + 1] - a[i] + 1]
    d += [b[i + 1] - b[i] + 1]
c += [n - a[-1] + a[0] + 1]
d += [n - b[-1] + b[0] + 1]
for i in range(k):
    if c == d[i:] + d[:i]:
        print("YES")
        break
else:
    print("NO")
