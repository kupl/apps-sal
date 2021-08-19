n = int(input())
b = input().split()
for x in range(n):
    b[x] = int(b[x])
b = sorted(b)
x = b.count(max(b))
y = b.count(min(b))
if max(b) != min(b):
    z = x * y
else:
    z = x * (x - 1) // 2
print(max(b) - min(b), z)
