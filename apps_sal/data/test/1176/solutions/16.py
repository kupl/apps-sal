n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(n):
    if a[i] < 0:
        c += 1
        a[i] = abs(a[i])
if c % 2 == 0:
    print(sum(a))
else:
    print(sum(a) - min(a) * 2)
