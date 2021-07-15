n, m, k = map(int, input().split())
a = list([])
for i in range(m + 1):
    l = int(input())
    a.append(l)
ans = 0
for i in range(m):
    bi = a[i] ^ a[m]
    s = bin(bi)
    r = 0
    j = 2
    while r <= k and j < len(s):
        if s[j] == '1':
            r += 1
        j += 1
    if r <= k:
        ans += 1
print(ans)
