from collections import defaultdict

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
cum = [0]*(N+1)
for i in range(1,N+1):
    cum[i] = cum[i-1] + A[i-1]
ans = 0
dic = defaultdict(int)
v_by_indx = defaultdict(int)
for i in range(N+1):
    if i-K >= 0:
        dic[v_by_indx[i-K]] -= 1
    diff = (cum[i]-i)%K
    ans += dic[diff]
    dic[diff] += 1
    v_by_indx[i] = diff
print(ans)

