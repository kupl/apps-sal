h, w = list(map(int, input().split()))
table = [list(input()) for _ in range(h)]

mx = [0, 1, 0, -1]#yとの兼ね合いで片方は0にして上下左右判定
my = [1, 0, -1, 0]#xとの兼ね合いで片方は0にして上下左右判定
for i in range(h):
    for j in range(w):
        if table[i][j] == "#":
            for k in range(4):
                tx = j + mx[k]#左右判定
                ty = i + my[k]#上下判定
                if 0 <= tx < w and 0 <= ty < h and table[ty][tx] == "#":#添え字に使えるか判定している
                    break
            else:#breakされなかった時実行される、上下左右に#がなかった時になる
                print("No")
                return
print("Yes")


