H,W,K = list(map(int,input().split()))
if K < H:
    print(K+1,1)
    return
K -= H
W -= 1
d,m = divmod(K,(W*2))
if m < W:
    print(H-2*d, 2+m)
else:
    m -= W
    print(H-1-2*d, W-m+1)

