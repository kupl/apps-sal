n, m = list(map(int, input().split()))

ans = 0
mat = []
for i in range(n):
    mat.append(input())
l = [0] * m

for j in range(m):
    for i in range(n):
        l[j] += (mat[i][j] == '1')

for i in range(n):
    flag = 0
    for j in range(m):
        if mat[i][j] == '1' and l[j] == 1:
            flag = 1
    if flag == 0:
        print("YES")
        return
print("NO")
