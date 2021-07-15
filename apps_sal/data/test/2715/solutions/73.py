K = int(input())
N = 50
if K <= 50:
    print(N)
    ans = [50]*K + [0]*(N-K)
    print(*ans)
    return

d,m = divmod(K,50)
ans = [d+49] * N
for i in range(N):
    if i < m:
        ans[i] += N-m+1
    else:
        ans[i] -= m
print(N)
print(*ans)
