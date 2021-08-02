import sys

n_rest, time = tuple(int(x) for x in sys.stdin.readline().split())
max_joy = -100000000000000000000

for i in range(n_rest):
    f, t = tuple(int(x) for x in sys.stdin.readline().split())
    cur_joy = 0
    if t > time:
        cur_joy = f - (t - time)
    else:
        cur_joy = f
    max_joy = max(max_joy, cur_joy)

print(max_joy)
