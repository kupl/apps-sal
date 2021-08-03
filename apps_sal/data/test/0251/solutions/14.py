towers, max_bite_size = list(map(int, input().strip().split()))
gen = list(map(int, input().strip().split()))

max_height = 2 * 10 ** 5

heights = [0] * (max_height)
for num in gen:
    heights[num - 1] += 1

num_blocks = 0

num_slices = 0
curr_slice_size = 0

block_sizes = [0] * (max_height)
for idx, num in enumerate(reversed(heights)):
    if num_blocks + num == towers:
        break
    num_blocks += num
    block_sizes[idx] = num_blocks
    if curr_slice_size + num_blocks > max_bite_size:
        num_slices += 1
        curr_slice_size = num_blocks
    else:
        curr_slice_size += num_blocks
if curr_slice_size > 0:
    num_slices += 1
best_so_far = num_slices


num_slices = 0
curr_slice_size = 0

for num in reversed(block_sizes):
    if curr_slice_size + num > max_bite_size:
        num_slices += 1
        curr_slice_size = num
    else:
        curr_slice_size += num
if curr_slice_size > 0:
    num_slices += 1

print(min(num_slices, best_so_far))
