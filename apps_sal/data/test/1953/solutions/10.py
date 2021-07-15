n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
s = 0
c = 0
for i in range(n):
    if s <= a[i]:
        c += 1
        s += a[i]
print(c)
