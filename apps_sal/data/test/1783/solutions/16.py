(n, k) = list(map(int, input().split()))
h = list(map(int, input().split()))
weeks = n - k + 1
max_sum = min(weeks, k)
s = 0
for i in range(1, n + 1):
    m = max_sum
    if i < max_sum:
        m = i
    elif n - i + 1 < max_sum:
        m = n - i + 1
    s += m * h[i - 1]
s /= weeks
print(s)
