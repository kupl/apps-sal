
l = []
for i in range(4):
    l.append(input())
ans = "NO"
for i in range(3):
    for j in range(3):
        x = l[i][j + 1] + l[i][j] + l[i + 1][j + 1] + l[i + 1][j]
        if(x.count('
            ans="YES"
print(ans)
