n = int(input())
a = list(map(int, input().split()))
sum = 0
p = []
for i in range(n):
    if a[i] % 2 == 0:
        sum += a[i]
    else:
        p.append(a[i])
p.sort()
if len(p) % 2 != 0:
    p.pop(0)
for t in range(len(p)):
    sum += p[t]
print(sum)

