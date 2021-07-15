n,m,c = map(int, input().split())
b = list(map(int, input().split()))
count = 0
for i in range(n):
    s = 0
    a = list(map(int, input().split()))
    for x in range(m):
        s += a[x]*b[x]
    s += c
    if s > 0:
        count += 1
print(count)
