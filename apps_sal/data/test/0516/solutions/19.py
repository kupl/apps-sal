# IAWT
n, m = list(map(int, input().split()))
s = input()
t = input()


def needs(i):
    x = 0
    for u in range(n):
        if t[i + u] != s[u]:
            x += 1
    return x


need = n
ind = 0
for i in range(m - n + 1):
    x = needs(i)
    if x < need:
        need = x
        ind = i

out = str(need) + '\n'
for i in range(n):
    if t[ind + i] != s[i]:
        out += str(i + 1) + ' '

print(out[:-1])
