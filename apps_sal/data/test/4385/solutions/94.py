import itertools
L = []
for i in range(5):
    L.append(int(input()))
k = int(input())

M = []
for v in itertools.combinations(L, 2):
    M.append(list(v))

dist = []
for m in M:
    dist.append(abs(m[0] - m[1]))

# print(dist)

if max(dist) > k:
    print(':(')
else:
    print('Yay!')
