n = int(input())
A = list(map(int, input().split()))

if n == 2:
    print(abs(A[0]-A[1]))
    return

cum_sum = [0]
for a in A:
    cum_sum.append(cum_sum[-1]+a)

ans = 10**9+1
for x in cum_sum[1:-1]:
    y = cum_sum[-1] - x
    ans = min(ans, abs(x-y))
print(ans)
