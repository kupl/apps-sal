n, x = map(int, input().split())
a = list(map(int, input().split()))
s = 0
t = 1
for i in range(n):
    s = s + a[i]
    if s <= x:
        t += 1
print(t)
