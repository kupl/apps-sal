n = int(input())
dirs = input()
goal = list(map(int, input().split(' ')))


def can(start, end, steps):
    dist = abs(start[0] - end[0]) + abs(start[1] - end[1])
    return dist <= steps and (steps - dist) % 2 == 0


if not can((0, 0), goal, n):
    print(-1)
    return

diffs = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}

pos = [(0, 0)] + [None] * n
for i, dir in enumerate(dirs):
    old_pos = pos[i]
    diff = diffs[dir]
    pos[i + 1] = (old_pos[0] + diff[0], old_pos[1] + diff[1])

final_pos = pos[n]

# best (minimum) segment to override to get to the solution
best = (abs(final_pos[0] - goal[0]) + abs(final_pos[1] - goal[1])) // 2

if best == 0:
    print(0)
    return

start = 0
end = best

current_best = float('inf')

while end <= n:
    # exclude segment and check if can reach without
    cur_pos = (
        pos[start][0] + final_pos[0] - pos[end][0],
        pos[start][1] + final_pos[1] - pos[end][1],
    )

    if can(cur_pos, goal, end - start):
        current_best = min(current_best, end - start)
        if current_best == best:
            break
        start += 1
    else:
        end += 1

print(current_best)


# min_steps = abs(goal[0]) + abs(goal[1])
# if min_steps > n or (min_steps - n) % 2 != 0:
#     print(-1)
#     return

# cur_pos = [0, 0]
# for dir in dirs:
#     if dir == 'U':
#         cur_pos[1] += 1
#     if dir == 'D':
#         cur_pos[1] -= 1
#     if dir == 'L':
#         cur_pos[0] -= 1
#     if dir == 'R':
#         cur_pos[0] += 1

# pos_diff = [goal[0] - cur_pos[0], goal[1] - cur_pos[1]]

# vertical = abs(pos_diff[1]) > abs(pos_diff[0])
# up = pos_diff[1] > 0
# right = pos_diff[0] > 0
# replacement_steps = (abs(pos_diff[0]) + abs(pos_diff[1])) // 2
# diagonal_walk = replacement_steps - \
#     abs(abs(pos_diff[1]) - abs(pos_diff[0])) // 2

# start, end = 0, 0
# covered = {'U': 0, 'D': 0, 'L': 0, 'R': 0}
# while end < n:
#     new_dir = dirs[end]
#     covered[new_dir] += 1
#     remaining = covered.copy()
#     end += 1

#     if vertical:
#         if up:
#             pass
#         else:
#             pass
#     else:
#         if right:
#             pass
#         else:
#             pass
