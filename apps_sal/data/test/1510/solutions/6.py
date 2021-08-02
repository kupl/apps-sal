n, m = map(int, input().split())
a, b = list(map(int, input().split())), list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
s = 0
for i in range(min(n, m)):
    if b[i] > a[i]: s += b[i] - a[i]
print(s)
