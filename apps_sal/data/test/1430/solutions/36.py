(N, K) = map(int, input().split())
S = input()
Nums = []
now = 1
cnt = 0
for i in range(N):
    if S[i] == str(now):
        cnt += 1
    else:
        Nums.append(cnt)
        now = 1 - now
        cnt = 1
if cnt != 0:
    Nums.append(cnt)
if len(Nums) % 2 == 0:
    Nums.append(0)
Add = 2 * K + 1
sum = [0] * (len(Nums) + 1)
for i in range(len(Nums)):
    sum[i + 1] = sum[i] + Nums[i]
ans = 0
for i in range(0, len(Nums), 2):
    left = i
    right = min(i + Add, len(Nums))
    tmp = sum[right] - sum[left]
    ans = max(tmp, ans)
print(ans)
