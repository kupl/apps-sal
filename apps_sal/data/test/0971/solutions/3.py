(n, b, d) = map(int, input().split())
arr = map(int, input().split())
d1 = 0
c = 0
for i in arr:
    if i <= b:
        d1 += i
    if d1 > d:
        c += 1
        d1 = 0
print(c)
