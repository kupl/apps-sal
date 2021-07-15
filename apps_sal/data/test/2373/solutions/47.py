n = int(input())
ls = list(map(int,input().split()))
di = []
ans = 0 
now = 0
for i in range(n):
    if ls[i] == i+1:
        now += 1
    else:
        if now != 0:
            di.append(now)
            now = 0
if now != 0:
    di.append(now)
for j in di:
    if j % 2 == 0:
        ans += j//2
    else:
        ans += (j//2) + 1
print(ans)

