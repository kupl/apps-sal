n = int(input())
(left, right) = (0, 0)
for i in range(n):
    (a, b) = list(map(int, input().split()))
    left += a
    right += b
left = min(n - left, left)
right = min(n - right, right)
print(left + right)
