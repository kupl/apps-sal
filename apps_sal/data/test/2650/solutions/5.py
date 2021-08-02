from heapq import heapify, heappop, heappush
N, Q = map(int, input().split())
where = []
rating = []
garten = [[] for _ in range(2 * 10**5)]  # 大きい順(マイナス掛け)
saikyo = []  # 小さい順
for i in range(N):
    A, B = map(int, input().split())
    where.append(B - 1)
    rating.append(A)
    heappush(garten[B - 1], (-A, i))  # (レート、園児)

for i in range(2 * 10**5):
    if not garten[i]:
        continue
    rate, num = garten[i][0]
    heappush(saikyo, (-rate, i))  # (レート、幼稚園)

for _ in range(Q):
    C, D = map(int, input().split())
    C, D = C - 1, D - 1  # 幼児、転園先

    moto = where[C]
    where[C] = D
    heappush(garten[D], (-rating[C], C))  # 転園先に追加
    if garten[D][0][1] == C:
        heappush(saikyo, (rating[C], D))

    while garten[moto]:  # 転園元の整理
        a, b = garten[moto][0]
        if where[b] == moto:
            break
        heappop(garten[moto])
    heappush(saikyo, (-a, moto))
    # print(garten[:5])
    while True:  # 最強リストの整理
        # print(saikyo)
        a, b = saikyo[0]
        if not garten[b]:
            heappop(saikyo)
            continue
        if garten[b][0][0] == -a:
            break
        heappop(saikyo)
    print(a)
