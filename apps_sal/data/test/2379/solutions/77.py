(n, k, c) = map(int, input().split())
s = input()
l = []
num = 0
i = 0
while num < k:
    if s[i] == 'o':
        l.append(i)
        num += 1
        i += c + 1
    else:
        i += 1
r = []
num = 0
i = n - 1
while num < k:
    if s[i] == 'o':
        r.append(i)
        num += 1
        i -= c + 1
    else:
        i -= 1
r.reverse()
for i in range(k):
    if l[i] == r[i]:
        print(l[i] + 1)
