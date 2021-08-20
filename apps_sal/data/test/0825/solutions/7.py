N = int(input())
pri_cnt = {}
n = N
i = 2
while i ** 2 <= N:
    while n % i == 0:
        if i not in pri_cnt:
            pri_cnt[i] = 1
        else:
            pri_cnt[i] += 1
        n = n / i
    if i == 2:
        i += 1
    else:
        i += 2
if n > 1:
    pri_cnt[int(n)] = 1
ans = 0
for (pri, cnt) in pri_cnt.items():
    count = 1
    remain = cnt
    while remain >= count:
        ans += 1
        remain -= count
        count += 1
print(ans)
