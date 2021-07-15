H, W = list(map(int, input().split()))

S = [list(input()) for _ in range(H)]

for h in range(H):
    for w in range(W):
        if S[h][w] == ".":
            continue
        
        if h != 0 and S[h-1][w] == "#":
            continue
        elif h != H-1 and S[h+1][w] == "#":
            continue
        elif w != 0 and S[h][w-1] == "#":
            continue
        elif w != W-1 and S[h][w+1] == "#":
            continue
        
        print("No")
        return

print("Yes")


