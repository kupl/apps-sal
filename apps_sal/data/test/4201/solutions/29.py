H, W, K = list(map(int, input().split()))
Square = [0] * H
for i in range(H):
    C = input()
    Square[i] = C
ans = 0
nowH = [0] * H
nowW = [0] * W
for j in range(2**H):
    for p in range(H):
        nowH[p] = j % 2
        j //= 2
    for k in range(2**W):
        kouho = 0
        for q in range(W):
            nowW[q] = k % 2
            k //= 2
        for s in range(H):
            for t in range(W):
                if nowH[s] == 0 and nowW[t] == 0 and Square[s][t] == "
                kouho += 1
        if kouho == K:
            ans += 1
print(ans)
