n, x = map(int, input().split())
cnt = [0 for i in range(100010)]
arr = list(map(int, input().split()))
for num in arr:
    cnt[num] += 1
ans = 0
for num in arr:
    xor_num = x ^ num
    if xor_num > 100000:
        continue
    cnt[num] -= 1
    if cnt[xor_num] > 0:
        ans += cnt[xor_num]
print(ans)
