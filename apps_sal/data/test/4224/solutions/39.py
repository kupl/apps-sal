N = int(input())
a = list(map(int,input().split()))

cnt = 0

for i in range(N):
    x = a[i]
    while(x%2==0):
        x = x // 2
        cnt += 1

print(cnt)
