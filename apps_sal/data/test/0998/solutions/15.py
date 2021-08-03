v = [0]
n, x = map(int, input().split())
e = [0] * (1 << 18)
e[0] = 1
for i in range(1, 1 << n):
    if e[x ^ i] == 1:
        continue
    e[i] = 1
    v.append(i)
print(len(v) - 1)
print(*[v[i] ^ v[i - 1] for i in range(1, len(v))])
