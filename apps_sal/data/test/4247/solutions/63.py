n = int(input())
p = list(map(int,input().split()))
cnt = 0
for i in range(1,n-1):
    if p[i-1] > p[i]:
        if p[i] > p[i+1]:
            cnt = cnt+1
    elif p[i+1] > p[i]:
        if p[i] > p[i-1]:
            cnt = cnt+1
print(cnt)
