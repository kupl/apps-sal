H,W = map(int,input().split())
s = [input() for _ in range(H)]
for i in range(1,H-1):
    for j in range(1,W-1):
        if s[i][j] == "#":
            if s[i][j-1] == "." and s[i][j+1] == "." and s[i-1][j] == "." and s[i+1][j] == ".":
                print("No")
                return
print("Yes")
