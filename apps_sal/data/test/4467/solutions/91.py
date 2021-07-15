
n = int(input().strip())
red = [list(map(int, input().split())) for i in range(n)]
blue = [list(map(int, input().split())) for j in range(n)]

for i in range(n):
    '''
    kagi_r = [min(red[i][0], red[i][1]), max(red[i][0], red[i][1])]
    kagi_b = [min(blue[i][0], blue[i][1]), max(blue[i][0], blue[i][1])]
    red[i] = red[i] + kagi_r
    blue[i] = blue[i] + kagi_b
    '''
red.sort(key=lambda x: (x[0], x[1]), reverse=True)
blue.sort(key=lambda x: x[1])
flg_r = [0]*n
cnt = 0

for i in range(n):
    for j in range(n):
        if flg_r[j]:
            continue
        if red[j][0] < blue[i][0] and red[j][1] < blue[i][1]:
            flg_r[j] = 1
            cnt += 1
            break

print(cnt)


