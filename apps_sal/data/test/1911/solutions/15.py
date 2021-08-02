n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
s = []
for q in range(n - 1):
    s.append([a[q + 1] - a[q], q])
s.sort(reverse=True)
d = {q[1] for q in s[:k - 1]}
ans = 0
q1 = a[0]
for q in range(n - 1):
    if q in d:
        ans += a[q] - q1
        q1 = a[q + 1]
print(ans + a[-1] - q1)
