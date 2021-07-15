n, l = map(int, input().split())
m = 1000
for i in range(l, l+n):
    if abs(i) < m:
        m = abs(i)
        a = i
print(sum(range(l, l+n)) - a)
