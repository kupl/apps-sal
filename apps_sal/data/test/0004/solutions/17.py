x = int(input())
arr = list(map(int, input().strip().split(' ')))
h = arr[0]
m = arr[1]
cnt = 0
while True:
    s = str(h)
    ss = str(m)
    if '7' in s or '7' in ss:
        break
    else:
        cnt += 1
        if m - x < 0:
            if h - 1 < 0:
                h = 23
            else:
                h -= 1
            m = 60 + m - x
        else:
            m = m - x
print(cnt)
