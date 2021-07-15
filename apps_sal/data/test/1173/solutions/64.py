from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = []
for _ in range(N):
    # 選手番号を0-indexにする
    line = list([int(x) - 1 for x in input().split()])
    A.append(line)

# cnt[i] = 選手iが現在までに何試合したか
cnt = [0] * N
# recent[i] = 選手iが最後に試合をした日
recent = [0] * N

# Qの初期値 = [0, 1, ..., N-1]
Q = deque(list(range(N)))

while Q:
    # ある選手(p1)について
    p1 = Q.popleft()
    # p1がまだ全試合(N-1試合)を終えていない場合
    # p2 = p1が次に当たるべき選手
    if cnt[p1] < N - 1:
        p2 = A[p1][cnt[p1]]
        # p2もまだ全試合を終えていない場合
        if cnt[p2] < N - 1:
            # p2が次に当たるべき選手がp1の場合 -> (p1,p2)の試合を行うことが可能
            if A[p2][cnt[p2]] == p1:
                # day = (p1,p2)の試合を行う日
                day = max(recent[p1], recent[p2]) + 1
                recent[p1] = day
                recent[p2] = day
                cnt[p1] += 1
                cnt[p2] += 1
                Q.append(p1)
                Q.append(p2)

if min(cnt) != N - 1:
    print((-1))
else:
    print((max(recent)))

