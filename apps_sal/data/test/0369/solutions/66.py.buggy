n, m = map(int, input().split())
sugoroku = input()[::-1]

cnt = 0
pos = 0
tmp = 0
lst = []
while pos != n:
    pos += 1
    cnt += 1
    if cnt == m:
        if sugoroku[pos] == "0":
            lst.append(cnt)
            cnt = 0
        else:
            if tmp == 0:
                print(-1)
                return
            lst.append(tmp)
            cnt -= tmp
            tmp = 0
    else:
        if sugoroku[pos] == "0":
            tmp = cnt
if cnt != 0:
    lst.append(cnt)
for num in lst[::-1]:
    print(num, end=" ")
