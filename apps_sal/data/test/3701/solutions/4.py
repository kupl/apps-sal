n, x, y = map(int, input().split())
s = input()
cnt, tmp = 0, 0
for i in s:
    if i == '1':
        if tmp:
            cnt += 1
        tmp = 0
    else:
        tmp += 1
if tmp:
    cnt += 1
if cnt > 0:
    print(min(x, y)*(cnt-1)+y)
else:
    print(0)
