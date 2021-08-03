n = int(input())
a = list(map(int, input().split()))
m = 0
for i in range(n):
    if a[i] < 0:
        m += 1
        a[i] = abs(a[i])
if m % 2 == 0:
    print(sum(a))
else:
    print(sum(a) - (min(a) * 2))
