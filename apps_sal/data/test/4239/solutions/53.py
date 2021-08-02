N = int(input())
ans = [0] * 100001
for i in range(6):
    ans[i] = i
s = 6
n = 9
for i in range(6, N + 1):
    p = i % 3
    if p != 0:
        ans[i] = ans[i - p] + p
    else:
        if i == s * 6:
            s *= 6
        if i == n * 9:
            n *= 9
        ans[i] = min(ans[i - s] + 1, ans[i - n] + 1)
print(ans[N])
