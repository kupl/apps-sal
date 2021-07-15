import heapq
X, Y, Z, K = list(map(int, input().split()))
A = sorted([int(i) for i in input().split()], reverse=True)
B = sorted([int(i) for i in input().split()], reverse=True)
C = sorted([int(i) for i in input().split()], reverse=True)

done = {(0, 0, 0)}

hq = [(-(A[0]+B[0]+C[0]), 0, 0, 0)]
heapq.heapify(hq)  # リストhqのheap化

ans = 0
D = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

for _ in range(K):
    s, i, j, k = heapq.heappop(hq)  # heap化されたリストhqから最小値を削除＆その最小値を出力
    print((-s))
    for d in D:
        ni, nj, nk = i+d[0], j+d[1], k+d[2]
        if ni < X and nj < Y and nk < Z and (ni, nj, nk) not in done:
            # heap化されたリストhqに要素xを追加
            heapq.heappush(hq, (-(A[ni]+B[nj]+C[nk]), ni, nj, nk))
            done.add((ni, nj, nk))

