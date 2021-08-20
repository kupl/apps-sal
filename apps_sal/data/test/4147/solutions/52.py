import itertools
(N, A, B, C) = list(map(int, input().split()))
l = [int(input()) for _ in range(N)]
ans = 10 ** 10
for x in itertools.product([0, 1, 2, 3], repeat=N):
    bamboo = [0] * 4
    tmp = 0
    for i in range(N):
        if x[i] in [1, 2, 3] and bamboo[x[i]] > 0:
            tmp += 10
        bamboo[x[i]] += l[i]
    if 0 in bamboo[1:]:
        continue
    tmp += abs(bamboo[1] - A) + abs(bamboo[2] - B) + abs(bamboo[3] - C)
    ans = min(ans, tmp)
print(ans)
