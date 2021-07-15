n = int(input())
l = list(map(int, input().split()))
ans = [0] * 101
for i in range(1, 101):
    for k in range(n):
        ans[i] += max(abs(l[k] - i) - 1, 0)
cnt = [100000000, 100000000]
for i in range(1, 101):
    if cnt[1] > ans[i]:
        cnt[0] = i
        cnt[1] = ans[i]
print(cnt[0], cnt[1])
