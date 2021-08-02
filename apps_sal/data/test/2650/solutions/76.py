from heapq import heappush, heappop

n, q = map(int, input().split())
rate = [0] * n
belong = [-1] * n
yochien_rates = [[] for i in range(2 * 10 ** 5 + 10)]
delete_yochien_rates = [[] for i in range(2 * 10 ** 5 + 10)]
yochiens = set()
for i in range(n):
    a, b = map(int, input().split())
    b -= 1
    rate[i] = a
    belong[i] = b
    yochiens.add(b)
    heappush(yochien_rates[b], -a)

maxs = []
delete_maxs = []

for i in yochiens:
    heappush(maxs, -yochien_rates[i][0])
ans = []
for _ in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1

    old = belong[c]
    belong[c] = d

    # 元いた幼稚園と新しい幼稚園の最強園児を削除キューに入れる
    heappush(delete_maxs, -yochien_rates[old][0])
    if yochien_rates[d]:
        heappush(delete_maxs, -yochien_rates[d][0])

    # 新しい幼稚園のratesと全体のratesの更新
    heappush(yochien_rates[d], -rate[c])
    heappush(maxs, -yochien_rates[d][0])

    # oldの更新
    heappush(delete_yochien_rates[old], -rate[c])
    while delete_yochien_rates[old] and yochien_rates[old][0] == delete_yochien_rates[old][0]:
        heappop(yochien_rates[old])
        heappop(delete_yochien_rates[old])
    if yochien_rates[old]:
        heappush(maxs, -yochien_rates[old][0])

    # 最小値計算
    while delete_maxs and maxs[0] == delete_maxs[0]:
        heappop(maxs)
        heappop(delete_maxs)
    ans.append(maxs[0])

print(*ans, sep='\n')
