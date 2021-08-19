(n, x, m) = map(int, input().split())
used = [0] * m
used[x] = 1
l = [x]
while True:
    x = x ** 2 % m
    if used[x] == 1:
        break
    else:
        used[x] = 1
        l.append(x)
a = len(l)
for i in range(a):
    if l[i] == x:
        b = i
        break
c = a - b
s = sum(l[b:])
s_ = sum(l[:b])
if n < b:
    print(sum(l[:n]))
else:
    print(s_ + s * ((n - b) // c) + sum(l[b:b + (n - b) % c]))
