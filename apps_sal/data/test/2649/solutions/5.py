n = int(input())
xy = [list(map(int, input().split())) for i in range(n)]
ans = []
l = [xy[i][0] + xy[i][1] for i in range(n)]
ans.append(max(l) - min(l))
l = [xy[i][0] - xy[i][1] for i in range(n)]
ans.append(max(l) - min(l))
l = [-xy[i][0] + xy[i][1] for i in range(n)]
ans.append(max(l) - min(l))
l = [-xy[i][0] - xy[i][1] for i in range(n)]
ans.append(max(l) - min(l))
print(max(ans))
