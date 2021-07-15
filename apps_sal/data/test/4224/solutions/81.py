n = int(input())
L = list(map(int,input().split()))

ans = 0
for i in range(n):
    cnt = 0
    while True:
        if L[i]%2 == 0:
            cnt +=1
            L[i]//=2
        else:
            break
    ans +=cnt
print(ans)
