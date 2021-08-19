import sys


def log(s):
    #    print(s)
    pass


k, a, b = list(map(int, sys.stdin.readline().strip().split(' ')))
alice = {}
for i in range(3):
    one, two, three = list(map(int, sys.stdin.readline().strip().split(' ')))
    alice[(i + 1, 1)] = one
    alice[(i + 1, 2)] = two
    alice[(i + 1, 3)] = three

bob = {}
for i in range(3):
    one, two, three = list(map(int, sys.stdin.readline().strip().split(' ')))
    bob[(i + 1, 1)] = one
    bob[(i + 1, 2)] = two
    bob[(i + 1, 3)] = three

score = {(1, 1): (0, 0), (2, 2): (0, 0), (3, 3): (0, 0),
         (1, 2): (0, +1), (2, 3): (0, +1), (3, 1): (0, 1),
         (2, 1): (1, 0), (3, 2): (1, 0), (1, 3): (1, 0)}

seen = []
current = (a, b)
while current not in seen:
    seen.append(current)
    current = (alice[current], bob[current])

loop = seen.index(current)
vals = [score[state] for state in seen]

a_point, b_point = (0, 0)
a_vals, b_vals = list(zip(*vals))
a_point += sum(a_vals[:min(k, loop)])
b_point += sum(b_vals[:min(k, loop)])

k = k - loop
loop_len = len(seen) - loop
a_loop_val = sum(a_vals[loop:])
b_loop_val = sum(b_vals[loop:])
if k >= 0:
    tail = k % loop_len
    num_iters = k // loop_len
    a_point += sum(a_vals[loop:loop + tail])
    b_point += sum(b_vals[loop:loop + tail])
    a_point += num_iters * a_loop_val
    b_point += num_iters * b_loop_val


log(a_point)
log(b_point)
print(round(a_point), round(b_point))
