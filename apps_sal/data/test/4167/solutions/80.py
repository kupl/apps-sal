n, k = list(map(int, input().split()))

num = [0] * (k + 1)
for i in range(1, n + 1):
    num[i % k] += 1

ans = 0
for a in range(1, n + 1):
    mod = a % k
    temp_mod = (k - mod) % k
    # print(temp_mod)
    if (temp_mod * 2) % k != 0:
        continue
    ans += num[temp_mod]**2
print(ans)
