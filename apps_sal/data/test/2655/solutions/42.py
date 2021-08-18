n = int(input())
friendry = list(map(int, input().split()))
friendry.sort()
friendry.reverse()
ans = 0
t = n - 1
for i in range(n - 1):
    lim = 2
    if(i == 0):
        lim = 1
    for j in range(lim):
        if(t > 0):
            ans += friendry[i]
            t -= 1

print(ans)
