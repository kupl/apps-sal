(n, k) = list(map(int, input().split()))
x = list(map(int, input().split()))
ans = 10 ** 9
for i in range(0, n - k + 1):
    if x[i] * x[i + k - 1] >= 0:
        ans_tmp = max(abs(x[i]), abs(x[i + k - 1]))
    else:
        ans_tmp = abs(x[i]) + abs(x[i + k - 1]) + min(abs(x[i]), abs(x[i + k - 1]))
    ans = min(ans, ans_tmp)
print(ans)
