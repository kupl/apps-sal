N = int(input())
F = [int(''.join(list(input().split())), 2) for i in range(N)]
P = [list(map(int, input().split())) for i in range(N)]
ans = -float('inf')
for i in range(1, 2 ** 10):
    res = 0
    for k in range(N):
        p = i & F[k]
        cnt = 0
        for j in range(10):
            if p >> j & 1:
                cnt += 1
        res += P[k][cnt]
    ans = max(ans, res)
print(ans)
