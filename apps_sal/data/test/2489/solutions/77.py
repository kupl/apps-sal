N = int(input())
A = list(map(int,input().split()))
A.sort()
M = 10**6+5
cnt = [0]*M
for x in A:
    if cnt[x] != 0:
        cnt[x] = 2
        continue
    for i in range(x,M,x):
        cnt[i] += 1
ans = 0
for i in A:
    if cnt[i] == 1:
        ans += 1
print(ans)
