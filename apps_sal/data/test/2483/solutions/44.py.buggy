N, C = list(map(int, input().split()))
tel = [[0, -1] for i in range(C)]
pro = [list(map(int, input().split())) for i in range(N)]
pro.sort()
for s, t, c in pro:
    for i in range(C):
        if tel[i][0] < s - 0.5 or tel[i][1] == c or tel[i][1] == -1:
            tel[i][0] = t
            tel[i][1] = c
            break
for i in range(C):
    if tel[i][1] == -1:
        print(i)
        return
print(C)
