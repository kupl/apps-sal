n = int(input())
l = list(map(int,input().split()))
l.sort()
ans = 0
for i in range(n - 2):
    for j in range(i,n-1):
        for k in range(j,n):
            if l[i] != l[j] and l[j] != l[k] and l[k] != l[i]:
                if l[i] + l[j] > l[k]:
                    ans += 1
print(ans)
