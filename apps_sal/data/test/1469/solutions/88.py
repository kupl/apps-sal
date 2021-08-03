from math import log2, floor
L = int(input())
ans = []

r = floor(log2(L))

for i in range(r):
    ans.append('{} {} {}'.format(i + 1, i + 2, 0))
    ans.append('{} {} {}'.format(i + 1, i + 2, 2**i))

for t in range(r - 1, -1, -1):
    if 2**r <= L - 2**t:
        ans.append('{} {} {}'.format(t + 1, r + 1, L - 2**t))
        L -= 2**t

print('{} {}'.format(r + 1, len(ans)))
for s in ans:
    print(s)
