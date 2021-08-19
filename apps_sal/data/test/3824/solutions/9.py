(n, k) = map(int, input().strip().split(' '))
(a, b) = map(int, input().strip().split(' '))
print(2 * (max(2, abs(a - n) + 1) + max(2, abs(b - k) + 1)))
