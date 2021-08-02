n, x = list(map(int, input().split()))
A = list(map(int, input().split()))
cnt = [0] * (n - 1)
ans1 = 0
for i in range(n - 1):
    cnt[i] = A[i] + A[i + 1]
    cnt[i] -= x
    cnt[i] = max(cnt[i], 0)
temp_cnt = cnt[::]
# print(cnt)
for i in range(n - 1):
    if temp_cnt[i] == 0:
        continue
    if i < n - 2:
        ans1 += temp_cnt[i]
        temp_cnt[i + 1] -= min(A[i + 1], temp_cnt[i])
        temp_cnt[i] = 0
        temp_cnt[i + 1] = max(temp_cnt[i + 1], 0)
    # print(ans1)
ans1 += temp_cnt[-1]


print(ans1)
