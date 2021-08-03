n = int(input())
a = [int(i) for i in input().split()]
b, v, ans = [], [], 0
for i in a:
    c = int(i ** (1 / 2))
    if c * c == i or (c + 1) * (c + 1) == i or (c - 1) * (c - 1) == i:
        b.append(i)
b.sort(reverse=True)
for i in range(len(b) - n // 2):
    if b[i] == 0:
        ans += 2
    else:
        ans += 1
for i in a:
    c = int(i ** (1 / 2))
    if c * c == i or (c + 1) * (c + 1) == i or (c - 1) * (c - 1) == i:
        continue
    v.append(min(i - c * c, (c + 1) * (c + 1) - i))
v.sort()
for i in range(n // 2 - len(b)):
    ans += v[i]
print(ans)
