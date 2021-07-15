n, k = map(int, input().split())
exist = [False] * 16
zero = [False] * 4
for i in range(n):
    part = list(map(int, input().split()))
    P = [0] * (4 - k)
    for elem in part:
        P.append(elem)
    num = 0
    for j in range(4):
        if P[j] == 0:
            zero[j] = True
    for j in range(4):
        if P[3 - j] == 1:
            num += 2 ** j
    exist[num] = True
ans = False
if exist[0] or (exist[1] and zero[3]) or (exist[2] and zero[2]) or (exist[4] and zero[1]) or (exist[8] and zero[0]) or (exist[3] and exist[12]) or (exist[5] and exist[10]) or (exist[6] and exist[9]):
    ans = True
if ans:
    print('YES')
else:
    print('NO')
