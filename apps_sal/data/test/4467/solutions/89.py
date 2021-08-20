"""
青はxの昇順、赤はyの降順に並び替え、xの小さい青からペアを探していく。x座標の検証において、小さい青の候補に入る赤は今後の青の候補にも
なるため、y座標ができるだけ大きい赤とペアを作るようにする。

"""
n = int(input())
red = [[0] * 2 for _ in range(n)]
blue = [[0] * 2 for _ in range(n)]
for i in range(n):
    (red[i][1], red[i][0]) = list(map(int, input().split()))
for i in range(n):
    (blue[i][0], blue[i][1]) = list(map(int, input().split()))
red.sort(reverse=True)
blue.sort()
ans = 0
usedred = [False] * n
for i in range(n):
    for j in range(n):
        if blue[i][0] > red[j][1] and blue[i][1] > red[j][0] and (usedred[j] != True):
            ans += 1
            usedred[j] = True
            break
print(ans)
