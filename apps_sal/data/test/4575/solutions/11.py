n = int(input())
d,x = map(int, input().split())
a=[]
for i in range(n):
    a.append(int(input()))

ans = 0
for i in a:
    cnt = 0
    days=1
    while days<=d:
        cnt+=1
        days+=i
    ans+=cnt
print(ans+x, flush=True)


