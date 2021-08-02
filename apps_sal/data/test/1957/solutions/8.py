num_holes, total_volume, desired_volume = (int(x) for x in input().split())
hole_sizes = [int(x) for x in input().split()]

unblocked_sizes = sum(hole_sizes)
sizes_to_block = list(reversed(sorted(hole_sizes[1:])))
num_blocked = 0

while hole_sizes[0] * total_volume < desired_volume * unblocked_sizes:
    unblocked_sizes -= sizes_to_block[num_blocked]
    num_blocked += 1

print(num_blocked)
