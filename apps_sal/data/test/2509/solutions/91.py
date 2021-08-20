(n, k) = list(map(int, input().split()))
ans = 0
for i in range(k + 1, n + 1):
    num = n // i
    ans_tmp = num * (i - k)
    ans_tmp += max(0, n % i - k + 1)
    if k == 0:
        ans_tmp -= 1
    ans += ans_tmp
print(ans)
