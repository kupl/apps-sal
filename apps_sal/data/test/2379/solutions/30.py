(n, k, c) = map(int, input().split())
s = input()
l = []
r = []
i = 0
j = 0
while len(l) < k and i < n:
    if s[i] == 'o':
        l.append(i + 1)
        i += c + 1
    else:
        i += 1
while len(r) < k and j < n:
    if s[-j - 1] == 'o':
        r.append(n - j)
        j += c + 1
    else:
        j += 1
for n in range(k):
    if l[n] == r[-n - 1]:
        print(l[n])
