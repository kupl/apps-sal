n = int(input())
d, x  = map(int, input().split())
a = []
[a.append(int(input())) for i in range(n)]
cnt = 0
for day in range(1, d+1):
    for eat in a:
         if (1+day*eat) <= d :
             cnt += 1
print(cnt+n+x)
