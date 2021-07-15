h,w = map(int,input().split())
s = [[0]*(w+2)]
for i in range(h):
  s += [[0]+list(input())+[0]]
s += [[0]*(w+2)]


for i in range(1,h+1):
    for j in range(1,w+1):
        cnt = 0
        if s[i][j]== "#":
            continue
        if s[i][j+1]=="#":
            cnt += 1
        if s[i][j-1] == "#":
            cnt += 1
        if s[i-1][j] == "#":
            cnt += 1
        if s[i-1][j+1] == "#":
             cnt += 1
        if s[i-1][j-1] == "#":
             cnt += 1
        if s[i+1][j] == "#":
            cnt += 1
        if s[i+1][j-1] == "#":
            cnt += 1
        if s[i+1][j+1] == "#":
            cnt += 1
        s[i][j] = cnt
    
for k in range(1,h+1):
  print(*s[k][1:-1],sep="")
