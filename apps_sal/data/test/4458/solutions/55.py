n = int(input())
p = list(map(int,input().split()))
ans = 0
for i in range(n):
    if (i == 0):
        ans = ans + 1
        x = p[0]
    else:
        if (x < p[i]):
            pass
        else:
            ans = ans + 1
            x = p[i]

print(ans)

