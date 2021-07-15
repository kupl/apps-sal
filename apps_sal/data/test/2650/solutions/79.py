from collections import defaultdict
import heapq

n, q = map(int, input().split())
kindergarten = defaultdict(lambda : [])

best = []
A, B = [], []

for i in range(n):
    a, b = map(int, input().split())
    A.append(a)  # スコア
    B.append(b)  # 幼稚園番号
    heapq.heappush(kindergarten[b], (-a, i))

for i in kindergarten:
    tmp = kindergarten[i][0]
    heapq.heappush(best, (-tmp[0], tmp[1]))

for i in range(q):
    c, d = map(int, input().split())  # c: 幼児の番号, d: 転園先の幼稚園番号
    kd_ori = B[c-1]
    B[c-1] = d

    while kindergarten[kd_ori]:
        x = kindergarten[kd_ori][0]
        if B[x[1]] != kd_ori:
            heapq.heappop(kindergarten[kd_ori])
            continue
        heapq.heappush(best, (-x[0], x[1]))
        break
    heapq.heappush(kindergarten[d], (-A[c-1], c-1))

    while kindergarten[d]:
        tmp = kindergarten[d][0]
        heapq.heappush(best, (-tmp[0], tmp[1]))
        break

    while best:
        tmp = best[0]

        tmp2 = kindergarten[B[tmp[1]]][0]
        if -tmp2[0] != tmp[0]:
            heapq.heappop(best)
            continue
        print(tmp[0])
        break

    print()
