I = input()

n = len(I)
left = 0
right = n - 1

block_left_index = 0
block_right_index = n

# Example:
# 000011000
# |     |
# or
# |    |
while left < right:
    if I[left] != I[left + 1]:
        block_left_index = left + 1
    if I[right] != I[right - 1]:
        block_right_index = right
    left += 1
    right -= 1

ans = min(n - block_left_index, block_right_index)
print(ans, flush=True)
