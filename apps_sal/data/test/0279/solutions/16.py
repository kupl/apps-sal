import sys

curr_speed, v2 = [int(s) for s in sys.stdin.readline().split()]
t, d = [int(s) for s in sys.stdin.readline().split()]

path = [curr_speed]
sec_left = t - 2

while sec_left:
    max_allowed = v2 + d * sec_left
    max_possible = curr_speed + d
    curr_speed = min(max_allowed, max_possible)
    path.append(curr_speed)
    sec_left -= 1

path.append(v2)
print(sum(path))

