n,m = list(map(int,input().split()))
ci = list(map(int,input().split()))
ai = list(map(int,input().split()))
i = 0
j = 0
ans = 0
while i < n and j < m:
    if ci[i] > ai[j]:
        i += 1
    else:
        i += 1
        j += 1
        ans += 1
print(ans)

