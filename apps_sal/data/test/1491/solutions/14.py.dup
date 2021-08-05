n = int(input())
a = [int(i) for i in input().split()]
b, v, ans = [], [], 0
for i in a:
    c = int(i ** (1 / 2))
    if c * c == i:
        b.append(i)
    else:
        v.append(min(i - c * c, (c + 1) * (c + 1) - i))
b.sort(reverse=True)
v.sort()
for i in range(len(b) - n // 2):
    ans += 1 + (b[i] == 0)
for i in range(n // 2 - len(b)):
    ans += v[i]
print(ans)
