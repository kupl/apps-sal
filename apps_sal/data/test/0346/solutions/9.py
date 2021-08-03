n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(len(b)):
    b[i] -= 1
b = set(b)
c = []
d = []
for i in range(len(a)):
    if i in b:
        c.append(a[i])
    else:
        d.append(a[i])
sum = 0
for i in range(len(d)):
    sum += d[i]
c = sorted(c)
if sum < c[-1]:
    sum += c[-1]
    sum *= (2**(len(c) - 1))
else:
    sum *= (2**len(c))
print(sum)
