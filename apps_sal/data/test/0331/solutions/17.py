(n, m, k) = list(map(int, input().split()))
m -= 1
print(10 * min((abs(i - m) for (i, c) in enumerate(map(int, input().split())) if 0 < c <= k)))
