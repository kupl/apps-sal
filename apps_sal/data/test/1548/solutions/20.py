n = int(input())
a = list(map(int, input().split()))
a.sort()
s = sum(a)
h = sum(a[n // 2:])
v = s - h
print(h * h + v * v)
