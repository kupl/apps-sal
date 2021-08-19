N, C = map(int, input().split())
prog = [list(map(int, input().split())) for _ in range(N)]

#tv[i] = [t, c]
tv = [[-1, 0] for i in range(C)]

prog.sort()

for p in prog:
    s, t, c = p
    for i in range(C):
        if tv[i][0] < s - 0.5 or tv[i][1] == c or tv[i][1] == 0:
            tv[i][0] = t
            tv[i][1] = c
            break


ans = 0
for i in range(C):
    if tv[i][0] > 0:
        ans += 1
    else:
        break

print(ans)
