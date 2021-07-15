n = int(input())
p = list(map(int,input().rstrip().split()))
pp = sorted(p)
cnt = 0
for i in range(n):
    if p[i]!=pp[i]:
        cnt+=1
if cnt>2:
    print("NO")
else:
    print("YES")
