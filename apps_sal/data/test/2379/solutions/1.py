(n, k, c) = map(int, input().split())
s = input()
l = []
r = []
i = 0
while len(l) < k:
    if s[i] == 'o':
        l.append(i)
        i += c + 1
    else:
        i += 1
i = 0
while len(r) < k:
    if s[n - 1 - i] == 'o':
        r.append(n - 1 - i)
        i += c + 1
    else:
        i += 1
for i in range(k):
    if l[i] == r[-i - 1]:
        print(l[i] + 1)
