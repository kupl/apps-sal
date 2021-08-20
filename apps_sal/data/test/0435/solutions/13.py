(n, k) = map(int, input().split())
s = input()
(e, t) = (0, 0)
res = 0
for i in range(n):
    if s[i] == 'b':
        t += 1
    while t > k and e < i:
        if s[e] == 'b':
            t -= 1
        e += 1
    res = max(res, i - e + 1)
(e, t) = (0, 0)
for i in range(n):
    if s[i] == 'a':
        t += 1
    while t > k and e < i:
        if s[e] == 'a':
            t -= 1
        e += 1
    res = max(res, i - e + 1)
print(res)
