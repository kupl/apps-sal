# ARC105 - A
cakes = [int(x) for x in input().split()]

# 普通の全探索でも解くことはできるが、練習のためにあえてbit全探索を用いて解いてみる
# ループ数は2**4 = 16回

for i in range(2**4):
    x, y = 0, 0
    for j in range(4):
        #print((i >> j)&1,end=" ")
        if (i >> j) & 1 == 1:
            x += cakes[j]
        else:
            y += cakes[j]

    if x == y:
        print("Yes")
        return
    # print()

print("No")
