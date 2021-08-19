(n, x, y) = map(int, input().split())
ss = input().strip()
L = len(ss)
i = 0
last = -1
cnt = 0
while i < L:
    if ss[i] == '1':
        if last == 0:
            cnt += 1
        last = 1
    else:
        last = 0
    i += 1
if ss[L - 1] == '0':
    cnt += 1
ans = 0
if x < y:
    ans = (cnt - 1) * x + y
else:
    ans = cnt * y
if cnt == 0:
    ans = 0
print(int(ans))
