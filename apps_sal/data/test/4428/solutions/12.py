n = int(input())
a = [int(x) for x in input().split()]
left = 0
right = n - 1
left_sum = 0
right_sum = 0
equal = 0
while left <= right and left < n and (right >= 0):
    if left_sum > right_sum:
        right_sum += a[right]
        right -= 1
    else:
        left_sum += a[left]
        left += 1
    if left_sum == right_sum:
        equal = left_sum
print(equal)
