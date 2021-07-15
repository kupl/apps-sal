C=[list(input()) for _ in range(2)]
flag=True
for i in range(2):
    for j in range(3):
        if C[i][j]!=C[1-i][2-j]:
            flag=False
if flag:
    print("YES")
else:
    print("NO")

