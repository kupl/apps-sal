n = int(input())
P = list(map(int, input().split()))
ans = 0
streak = 0
for i in range(1, n):
    #print (P[i])
    if P[i-1] >= P[i]:
        streak += 1
    else:
        ans = max(ans, streak)
        streak = 0
ans = max(ans, streak)
print (ans)
