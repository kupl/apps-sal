n, k = list(map(int, input().split()))
a = []
for _ in range(n):
    z = int(input())
    a.append(z)
if n % 2:
    a.append(0)
a.sort()
i = 0
res = 0
ost = 0
while i < len(a) - 1:
    if a[i] == a[i + 1]:
        i += 2
        res += 2
    else:
        i += 1
        ost += 1
if ost % 2:
    print(res + (ost + 1) // 2)
else:
    print(res + ost // 2)
