a, b, k = list(map(int, input().split()))

rem_a = max(a - k, 0)
k = max(k - a, 0)
rem_b = max(b - k, 0)

print((str(rem_a) + ' ' + str(rem_b)))

