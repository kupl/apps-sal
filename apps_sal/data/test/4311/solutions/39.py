S = int(input())

a = [S]
cnt = 1
while True:
    if S % 2 == 0:
        S /= 2
    else:
        S = 3 * S + 1
    cnt += 1
    if S in a:
        break
    else:
        a.append(S)

print(cnt)
