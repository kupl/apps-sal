import sys
H, W = map(int, input().split())
if H == 1:
    if W == 1:
        s = input()
        if s == "#":
            print("#")
        else:
            print(0)
    else:
        cnt = [0 for _ in range(W)]
        s = list(input())
        for w in range(W):
            if w == 0:
                cnt[w] += s[w+1] == "#"
            elif w == W-1:
                cnt[w] += s[w-1] == "#"
            else:
                cnt[w] += s[w+1] == "#"
                cnt[w] += s[w-1] == "#"
        for w in range(W):
            if s[w] == "#":
                cnt[w] = "#"
        ans = map(str, cnt)
        print("".join(ans))
    return
if W == 1:
    cnt = [0 for _ in range(H)]
    s = []
    for h in range(H):
        s.append(input())
    for h in range(H):
        if h == 0:
            cnt[h] += s[h+1] == "#"
        elif h == H-1:
            cnt[h] += s[h-1] == "#"
        else:
            cnt[h] += s[h-1] == "#"
            cnt[h] += s[h+1] == "#"
    for h in range(H):
        if s[h] == "#":
            print("#")
        else:
            print(cnt[h])
    return
    
S = []
cnt = [[0 for _ in range(W)] for _ in range(H)]
for h in range(H):
    s = list(input())
    for w in range(W):
        if w == 0:
            cnt[h][w] += s[w+1] == "#"
        elif w == W-1:
            cnt[h][w] += s[w-1] == "#"
        else:
            cnt[h][w] += s[w+1] == "#"
            cnt[h][w] += s[w-1] == "#"
    S.append(s)
    
for h in range(H):
    for w in range(W):
        if h == 0:
            cnt[h][w] += S[h+1][w] == "#"
            if w == 0:
                cnt[h][w] += S[h+1][w+1] == "#"
            elif w == W-1:
                cnt[h][w] += S[h+1][w-1] == "#"
            else:
                cnt[h][w] += S[h+1][w-1] == "#"
                cnt[h][w] += S[h+1][w+1] == "#"
        elif h == H-1:
            cnt[h][w] += S[h-1][w] == "#"
            if w == 0:
                cnt[h][w] += S[h-1][w+1] == "#"
            elif w == W-1:
                cnt[h][w] += S[h-1][w-1] == "#"
            else:
                cnt[h][w] += S[h-1][w-1] == "#"
                cnt[h][w] += S[h-1][w+1] == "#"
        else:
            cnt[h][w] += S[h+1][w] == "#"
            if w == 0:
                cnt[h][w] += S[h+1][w+1] == "#"
            elif w == W-1:
                cnt[h][w] += S[h+1][w-1] == "#"
            else:
                cnt[h][w] += S[h+1][w-1] == "#"
                cnt[h][w] += S[h+1][w+1] == "#"
            cnt[h][w] += S[h-1][w] == "#"
            if w == 0:
                cnt[h][w] += S[h-1][w+1] == "#"
            elif w == W-1:
                cnt[h][w] += S[h-1][w-1] == "#"
            else:
                cnt[h][w] += S[h-1][w-1] == "#"
                cnt[h][w] += S[h-1][w+1] == "#"
                
for h in range(H):
    s = S[h]
    for w in range(W):
        if s[w] == "#":
            cnt[h][w] = "#"
    ans = map(str, cnt[h])
    print("".join(ans))
