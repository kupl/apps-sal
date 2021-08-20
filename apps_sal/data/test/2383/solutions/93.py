N = int(input())
con = 1
set = 0
s = list(map(int, input().split()))
for i in s:
    if con == i:
        set += 1
        con += 1
if set == 0:
    print(-1)
else:
    ans = len(s) - set
    print(ans)
