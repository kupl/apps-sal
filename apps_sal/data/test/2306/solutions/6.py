import numpy as np
N = int(input())
T = list(map(int, input().split()))
V = list(map(int, input().split()))
FT = sum(T) * 2 + 1
limit = []
cumt = 0
for n in range(2 + N):
    if n == 0:
        lis = [0.5 * i for i in range(FT)]
    elif n == 1:
        lis = [0.5 * i for i in range(FT)][::-1]
    else:
        t = T[n - 2]
        v = V[n - 2]
        lis = [v + cumt // 2 - 0.5 * i for i in range(cumt)] + [v for _ in range(t * 2)] + [v + i * 0.5 for i in range(FT - cumt - t * 2)]
        cumt += t * 2
    limit.append(lis)
limit = np.min(np.array(limit), axis=0)
ans = 0
for i in range(FT - 1):
    ans += (limit[i + 1] + limit[i]) * 0.25
print(ans)
