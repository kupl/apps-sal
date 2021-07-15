h, w, k = map(int, input().split())
fig = [list(input()) for  _ in range(h)]

count = 0
import itertools
for r_paint in itertools.product([0,1], repeat=h): #0:その行を塗りつぶさない 1:その行を塗りつぶす
    for c_paint in itertools.product([0,1], repeat=w): # column
        kuro = 0 #黒塗りの数を数える
        for row in range(h):
            for col in range(w):
                if (fig[row][col] == "#") and (r_paint[row] == 0) and (c_paint[col] == 0): #黒いマスかつ塗りつぶされていない
                    kuro += 1
        if kuro == k:
            count += 1

print(count)
