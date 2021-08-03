n = int(input())
s = list(map(int, input().split()))
MINUS_INF = -float("inf")
ans = 0
for c in range(1, n):
    k = 1
    tmp_ans = 0
    while k * c < n - 1:
        a = (n - 1) - k * c
        b = a - c
        if a <= b or b <= 0:
            tmp_ans = MINUS_INF
        if a % c == 0 and a // c <= k:
            tmp_ans = MINUS_INF
        tmp_ans += s[n - 1 - k * c] + s[k * c]
        ans = max(ans, tmp_ans)
        k += 1
print(ans)
