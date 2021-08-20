k = int(input())
(a, b) = map(int, input().split())
print(['NG', 'OK'][b - b % k >= a])
