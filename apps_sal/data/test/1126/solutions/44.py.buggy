n, x, m = map(int, input().split())
l = [x]
s = {x}
for i in range(n):
    x = x * x % m
    if x in s:
        break
    l += [x]
    s.add(x)
xi = 0
for i in range(len(l)):
    if x == l[i]:
        xi = i
        break
ans = 0
if n <= xi:
    print(sum(l[:n]))
    return
ans = sum(l[:xi])
n -= xi
l = l[xi:]
print(ans + sum(l) * (n // len(l)) + sum(l[:(n % len(l))]))
