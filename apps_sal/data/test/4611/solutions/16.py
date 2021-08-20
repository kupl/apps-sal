N = int(input())
l = []
now = [0, 0, 0]
ans = 'Yes'
for _ in range(N):
    inp = list(map(int, input().split()))
    l.append(inp)
for i in range(N):
    shortest = abs(l[i][1] - now[1]) + abs(l[i][2] - now[2])
    if shortest > l[i][0] - now[0]:
        ans = 'No'
        break
    a = l[i][0] - now[0] - shortest
    if a % 2 != 0:
        ans = 'No'
        break
    else:
        now = l[i]
print(ans)
