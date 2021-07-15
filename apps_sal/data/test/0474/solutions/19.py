n = int(input())

a = list(map(int, input().split()))

mx = max(a)

c = 0
mc = 0

for i in range(n):
    if a[i] == mx:
        c += 1
        mc = max(mc, c)
    else:
        mc = max(mc, c)
        c = 0
print(mc)
