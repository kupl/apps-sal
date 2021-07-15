n = int(input())
l = list(map(int, input().split()))
ans = 1
cnt = 1
start = False
for i in l:
    if i == 1:
        start = True
        ans *= cnt
        cnt = 1
    if i == 0 and start:
        cnt += 1
if l.count(1) == 0:
    print(0)
else:
    print(ans)

