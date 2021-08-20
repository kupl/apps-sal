n = int(input())
nums = list(map(int, input().split()))
nums.sort()
ans = 0
cnt = {}
flag = [0] * 1000005
for i in nums:
    cnt[i] = cnt.get(i, 0) + 1
for i in nums:
    if flag[i] == 0 and cnt[i] == 1:
        ans += 1
    if flag[i] == 1:
        continue
    for j in range(i, 1000001, i):
        flag[j] = 1
print(ans)
