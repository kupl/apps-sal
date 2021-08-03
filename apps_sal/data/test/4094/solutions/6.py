K = int(input())

i = 7 % K
se = set([i])
cnt = 1
while True:
    if i == 0:
        print(cnt)
        break
    cnt += 1
    i = (i * 10 + 7) % K
    if i in se:
        print((-1))
        break
    else:
        se.add(i)
