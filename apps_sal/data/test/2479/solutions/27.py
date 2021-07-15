n, q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(q)]

v = n-1 # 最も上にある白石のy座標
h = n-1 # 最も左にある白石のx座標
tate = [n-1] * n
yoko = [n-1] * n
ans = (n-2)**2
for q1, q2 in queries:
    q2 -= 1
    if q1 == 1:
        # タテの処理
        if q2 < h:
            ans -= v-1
            # 左上の矩形より外は、更新されることがなくなったらtate yokoに格納
            # それぞれの更新は高々n回
            for i in range(h, q2, -1):
                tate[i] = v
            h = q2
        else:
            ans -= tate[q2]-1
    else:
        #  ヨコの処理
        if q2 < v:
            ans -= max(0, h-1)
            for i in range(v, q2, -1):
                yoko[i] = h
            v = q2
        else:
            ans -= yoko[q2]-1
print(ans)
