N = int(input())
con = [0]
vert = [i for i in range(1, N + 1)]
a = input().split(' ')
for i in range(N - 1):
    con.append(int(a[i]) - 1)
color = []
a = input().split(' ')
for i in range(N):
    color.append(int(a[i]))
cur = [color[0] for i in range(N)]
steps = 1
for i in range(1, N):
    if cur[con[i]] == color[i]:
        cur[i] = color[i]
    else:
        steps += 1
        cur[i] = color[i]
print(steps)
