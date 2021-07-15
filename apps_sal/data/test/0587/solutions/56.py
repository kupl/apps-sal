import heapq

N, K = list(map(int, input().split()))
sushi = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1], reverse=True)

eaten = [False]*N

#d1: 種類が増えないもの同士、d2: 同じ種類の中で最大の組み合わせ
d1, d2 = [0], [0]

for i in range(N):
    t, d = sushi[i]
    t -= 1
    if eaten[t]:
        d1.append(d1[-1]+d)
    else:
        eaten[t] = True
        d2.append(d2[-1]+d)


ans = 0
for i in range(1, K+1):
    if K-i >= len(d1):
        continue
    if i >= len(d2):
        continue
    ans = max(ans, d1[K-i]+d2[i]+i**2)
print(ans)

