n = int(input())
a = list(map(int,input().split()))
j = 1
ans = 0
for i in a:
    if i == j:
        j += 1
    else:
        ans += 1
if j == 1:
    print(-1)
else:
    print(ans)
