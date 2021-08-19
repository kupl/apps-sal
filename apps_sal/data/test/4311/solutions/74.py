s = int(input())
cnt = 1
S = [s]
while 1:
    cnt += 1
    if s % 2 == 0:
        s //= 2
    else:
        s = 3 * s + 1
    if s in S:
        print(cnt)
        break
    S.append(s)
