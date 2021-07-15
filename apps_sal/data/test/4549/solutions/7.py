h,w = list(map(int, input().split()))
s = [input() for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            flag = False
            for i_new, j_new in [(i+1, j), (i-1, j), (i,j+1), (i,j-1)]:
                if i_new<0 or i_new>=h or j_new<0 or j_new>=w: continue
                if s[i_new][j_new] == "#":
                    flag = True
                    break
            if not flag:
                print("No")
                return
print("Yes")

