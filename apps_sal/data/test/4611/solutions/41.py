# 最短でたどり着いたとして目的の時間までの残り時間が奇数ならばNo
# あとそもそも時間を使ってもたどりつけない場合もNo
n = int(input())
pos = [0, 0]
time = 0
for _ in range(n):
    t, x, y = list(map(int, input().split()))
    # 最短でたどりつく時間
    dist = abs(pos[0] - x) + abs(pos[1] - y)
    # そもそもたどりつけない場合
    if t - time < dist:
        print("No")
        return
    # 偶奇性
    rest = t - time
    if rest % 2 != dist % 2:
        print("No")
        return
    time = t
    pos = [x, y]
print("Yes")
