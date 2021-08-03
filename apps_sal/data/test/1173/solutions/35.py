import sys
readline = sys.stdin.readline

N = int(readline())
A = [None] * N
for i in range(N):
    # 後ろからpopできるように逆順リストで持つ
    A[i] = list(map(lambda x: x - 1, map(int, readline().split())))[::-1]

# 今日試合ができる可能性がある人リスト
candi = set(range(N))

day = 0
while candi:
    day += 1
    nex = set()
    done = set()
    for player in candi:
        if player in done:
            continue
        # player が試合できるかチェック
        if len(A[player]) == 0:
            continue
        rival = A[player][-1]
        if rival in done:
            continue
        if A[rival][-1] == player:
            # 試合できる
            A[player].pop()
            A[rival].pop()
            if A[player]:
                nex.add(player)
            done.add(player)
            if A[rival]:
                nex.add(rival)
            done.add(rival)
    if len(done) == 0:
        # 一試合もできなかった
        print(-1)
        return
    candi = nex

print(day)
