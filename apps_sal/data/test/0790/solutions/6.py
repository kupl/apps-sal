N, K = map(int, input().split())
A = list(map(int, input().split()))
D = list(map(int, input().split()))

suf_min = [None]*N
suf_min[-1] = A[-1]
suf_sum = [None]*N
suf_sum[-1] = A[-1]
suf_ans = [None]*N
suf_ans[-1] = max(A[-1] - D[-1], 0)
for i in range(N-2, -1, -1):
    suf_min[i] = min(A[i], suf_min[i+1])
    suf_sum[i] = suf_sum[i+1] + A[i]
    suf_ans[i] = max(suf_ans[i+1], suf_sum[i]-D[i])
    # print(i, suf_ans[i])

if K >= 2:
    print(max(0, sum(A) - min(*D[:-1]), suf_ans[0]))
    return

if K == 0:
    print(max(suf_ans[0], 0))
    return

pre_min = D[0]
pre_sum = 0
ans = max(0, sum(A) - D[0] - suf_min[0])
for i in range(N-1):
    pre_sum += A[i]
    pre_min = min(pre_min, D[i])
    ans = max(ans, pre_sum - pre_min + suf_ans[i+1], suf_ans[i+1])
print(max(0, ans))
