n = int(input())

m = 0
for i in range(n):
    x, y = (int(j) for j in input().split())
    if x + y > m:
        m = x + y
print(m)
