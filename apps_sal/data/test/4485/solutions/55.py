(N, M) = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]
res = []
for (a, b) in AB:
    if a == 1:
        res.append(b)
    if b == N:
        res.append(a)
print('IMPOSSIBLE' if len(res) == len(set(res)) else 'POSSIBLE')
