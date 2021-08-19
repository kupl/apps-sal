n = int(input())
left = 0
right = 0
for i in range(n):
    (left_cup, right_cup) = map(int, input().split())
    left += left_cup
    right += right_cup
left_close = n - left
right_close = n - right
left_time = min(left_close, left)
right_time = min(right_close, right)
print(left_time + right_time)
