H,W = map(int,input().split())
s = []
for i in range(H):
    a = list(input())
    s.append(a)
for i in range(H):
    for j in range(W):
        count = 0
        if s[i][j] == ".":
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    if (0 <= k <= H-1) and (0 <= l <= W-1) and s[k][l] == "#":
                        count += 1
            s[i][j] = str(count)
for i in range(H):
    print("".join(s[i]))
