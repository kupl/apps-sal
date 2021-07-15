n = int(input())
a = list(map(int,input().split()))
cnt = [0] * 101
for i in a:
    cnt[i] +=1
ans = [0] * 100
for i in range(n-1,-1,-1):
    for j in range(100,0,-1):
        if cnt[j]>0:
            ans[i] = j
            cnt[j]-=1
            break
print(*ans[:n])
