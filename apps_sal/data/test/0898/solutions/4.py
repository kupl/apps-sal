(n, m) = list(map(int, input().split()))
d = []
f = 1
while f * f < m + 1:
    if m % f == 0:
        d.append(f)
        d.append(m // f)
    f += 1
d.sort(reverse=True)
for i in d:
    if m - i * n >= 0 and (m - i * n) % i == 0:
        break
print(i)
