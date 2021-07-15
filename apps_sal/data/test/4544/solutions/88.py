import sys
N = int(input())
A = list(map(int, input().split()))

if N == 1:
    print(1)
    return
    
cnt = [0 for _ in range(10**5+1)]
for a in A:
    if a == 0:
        cnt[a] += 1
        cnt[a+1] += 1
    else:
        cnt[a-1] += 1
        cnt[a] += 1
        cnt[a+1] += 1
    
print(max(cnt))
