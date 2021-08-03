n = int(input())
L = list(map(int, input().split()))
r = 0
ans = 0
for i in range(n):
    if(L[i] == -1):
        if(r == 0):
            ans += 1
        else:
            r -= 1
    else:
        r += min(L[i], 10)
print(ans)
