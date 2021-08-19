(k, n) = list(map(int, input().split()))
cnt = [0] * (n + 1)
cmb = 0
a = list(map(int, input().split()))
ans = 10 ** 6 + 1
for i in range(n):
    r_idx = (i + 1) % n
    r_ans = a[i] + (k - a[r_idx]) if a[i] < a[r_idx] else abs(a[r_idx] - a[i])
    l_idx = (i - 1 + n) % n
    l_ans = k - a[i] + a[l_idx] if a[i] > a[l_idx] else a[l_idx] - a[i]
    ans = min([ans, r_ans, l_ans])
print(ans)
