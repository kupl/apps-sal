c = [list(map(int, input().split())) for _ in range(3)]
ans = "Yes"
for i in range(1,3):
    if c[i][0]-c[0][0] != c[i][1]-c[0][1] or c[i][1]-c[0][1] != c[i][2]-c[0][2]:
        ans = "No"
print(ans)
