n = int(input())
ai = list(map(int,input().split()))
ans = -1
for i in range(n):
    ai[i] -= (i)
    if ai[i] <= 0:
        ans = i+1
        break
if ans == -1:
    mini = 10**9
    for i in range(n):
        temp = ai[i] /  n
        if temp != int(temp):
            temp += 1
        if mini > int(temp):
            mini = int(temp)
            ans = i+1
print(ans)

