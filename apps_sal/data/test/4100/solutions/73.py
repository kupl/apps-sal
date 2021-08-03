N, K, Q = map(int, input().split())
ans = [0] * (N + 1)
for i in range(Q):
    ans[int(input())] += 1
sum_ans = sum(ans)
for i in range(1, N + 1):
    print('Yes' if K - (sum_ans - ans[i]) > 0 else 'No')
