from itertools import product
(N, A, B, C) = map(int, input().split())
l = []
for _ in range(N):
    l.append(int(input()))
ans = 10 ** 18
for i in product(range(4), repeat=N):
    mp = 0
    bamboo = [0, 0, 0]
    for j in range(N):
        s = i[j]
        if s == 3:
            continue
        else:
            if bamboo[s] != 0:
                mp += 10
            bamboo[s] += l[j]
    if bamboo[0] == 0 or bamboo[1] == 0 or bamboo[2] == 0:
        continue
    mp += abs(A - bamboo[0])
    mp += abs(B - bamboo[1])
    mp += abs(C - bamboo[2])
    ans = min(ans, mp)
print(ans)
