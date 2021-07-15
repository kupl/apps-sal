N = int(input())
A = list(map(int, input().split()))
 
M = 10**6 + 1
 
cnt = [0] * M
 
for a in A:
    if cnt[a] != 0:
        cnt[a] += 1
        continue
    for b in range(a, M, a):
        cnt[b] += 1
 
ans = 0
for a in A:
    if cnt[a] == 1:ans += 1
 
print(ans)
