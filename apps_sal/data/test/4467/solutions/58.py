def resolve():
    import sys
    
    readline = sys.stdin.readline    # 1行だけ文字列にする

    N = int(readline())

    # 赤，青点をx,y座標の2次元リストとして入力
    red = [list(map(int, readline().split())) for _ in [0] * N]
    blue = [list(map(int, readline().split())) for _ in [0] * N]

    # 赤はy座標で降順ソート，青はx座標で昇順ソート
    red.sort(key=lambda x: x[1], reverse=True)
    blue.sort()

    ans = 0
    for c, d in blue:
        for a, b in red:
            if a <= c and b <= d:
                ans += 1
                red.remove([a, b])
                break
    print(ans)


resolve()

