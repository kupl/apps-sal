(n, k, c) = map(int, input().split())
s = list(input())
(i, cnt) = (0, 0)
l = []
while cnt < k:
    if s[i] == 'o':
        l.append(i + 1)
        cnt += 1
        i += c
    i += 1
(i, cnt) = (n - 1, 0)
r = []
while cnt < k:
    if s[i] == 'o':
        r.append(i + 1)
        cnt += 1
        i -= c
    i -= 1
r.sort()
for i in range(len(r)):
    if l[i] == r[i]:
        print(r[i])
