n = int(input())
t,a = map(int,input().split())
h = list(map(int,input().split()))

index = 0
ans = 10**10
cnt = 0
for i in range(n):
    temp = t-h[i]*0.006
    if ans > abs(a-temp):
        ans = abs(a-temp)
        cnt = i+1
print(cnt)
