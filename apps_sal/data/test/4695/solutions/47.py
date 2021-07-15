gr = [0,1,3,1,2,1,2,1,1,2,1,2,1]
x, y = map(int, input().split())
ans = 'Yes' if gr[x] == gr[y] else 'No'
print(ans)
