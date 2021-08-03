n, m, k = list(map(int, input().split()))

if (n - m) >= n // k:
    print(m)
else:
    longest_correct_streak = n - k * (n - m)
    p = longest_correct_streak // k
    print((k * (pow(2, p + 1, 1000000009) - 2) + (longest_correct_streak % k) + (n - m) * (k - 1)) % 1000000009)
