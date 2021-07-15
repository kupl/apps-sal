n = int(input())
m = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
a = sorted(a)
max_i = max(a) + m
for i in range(m):
    a[0] += 1
    a = sorted(a)
min_i = max(a)
print(min_i, max_i)
