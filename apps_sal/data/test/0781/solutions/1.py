def checkvalid(u, d):
    for i in range(8):
        cnt = 0
        for j in range(8):
            if u[j] != d[i + j]:
                cnt += 1
            if j >= 1 and (u[j] == u[j - 1] or d[i + j] == d[i + j - 1]):
                cnt = 0
                break
        if cnt == 8:
            return True
    return False


u = input()
d = input()
cnt = 2
isvalid = True

isvalid = checkvalid(u, d + d)
while cnt <= 7:
    cnt += 1
    u = d
    d = input()
    isvalid = isvalid and checkvalid(u, d + d)
if isvalid:
    print('YES')
else:
    print('NO')
