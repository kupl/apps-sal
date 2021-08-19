n = int(input())
s = 0
mi = 1000000000.0
for i in range(n):
    (a, p) = map(int, input().split())
    mi = min(mi, p)
    s += a * mi
print(s)
