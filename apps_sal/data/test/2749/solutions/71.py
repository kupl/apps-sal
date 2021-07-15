H, W = list(map(int, input().split()))
N = int(input())
A = list(map(int, input().split()))
ans = [[0]*W for _ in range(H)]
h = 0
w = 0
for i, a in enumerate(A):
    for _ in range(a):
        if w == W:
            h += 1
            w = 0
        
        if h % 2 != 0:
            ind = W-w-1
        else:
            ind = w
        ans[h][ind] = i+1
        w += 1
for _ in range(H):
    print((*ans[_]))

