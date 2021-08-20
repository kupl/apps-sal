n = int(input())
d = {}
for i in range(26):
    d[chr(ord('a') + i)] = 10 ** 9
for i in range(n):
    s = input()
    for j in range(26):
        d[chr(ord('a') + j)] = min(d[chr(ord('a') + j)], s.count(chr(ord('a') + j)))
ans = ''
for e in list(d.items()):
    ans += e[0] * e[1]
print(ans)
