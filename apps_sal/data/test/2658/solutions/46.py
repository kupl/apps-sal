from collections import deque


def solve(A, K):
    a = deque()  # 繰り返し部分
    seen = [False for _ in range(len(A))]  # 一度見たかどうか
    cur = 0
    while True:
        # 一度通った頂点を見つけたときの処理
        if seen[cur]:
            while a[0] != cur:
                # 最初の余計な数手分を除去する
                K -= 1
                a.popleft()

                # K が限界になったらリターン
                if K == 0:
                    return a[0] + 1
            break

        # 最初は愚直にシミュレーションしつつ、履歴をメモしていく
        a.append(cur)
        seen[cur] = True
        cur = A[cur]
    return a[K % len(a)] + 1


N, K = map(int, input().split())
A = list(map(int, input().split()))
A = [v - 1 for v in A]
print(solve(A, K))
