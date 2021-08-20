N = int(input())
a = list(map(int, input().split()))
targetnum = 1
breaknum = 0
for i in range(N):
    if a[i] == targetnum:
        targetnum += 1
    else:
        breaknum += 1
if breaknum == N:
    print(-1)
else:
    print(breaknum)
