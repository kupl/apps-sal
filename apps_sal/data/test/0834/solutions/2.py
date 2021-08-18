import sys

n = int(sys.stdin.readline())
a = list([int(x) - 1 for x in sys.stdin.readline().split()])

path_lens = []
cycle_lens = []
for i, v in enumerate(a):
    cur = i
    visited = []
    while cur not in visited:
        visited.append(cur)
        cur = a[cur]
    visited.append(cur)

    path_len = 0
    for j, x in enumerate(visited):
        if x in visited[j + 1:]:
            break
        path_len += 1
    cycle_len = len(visited) - path_len - 1

    path_lens.append(path_len)
    cycle_lens.append(cycle_len)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


to_start = max(path_lens)
lcm = 1
for i, v in enumerate(cycle_lens):
    lcm = lcm * v // gcd(lcm, v)


res = to_start
if to_start % lcm > 0 or to_start == 0:
    res += lcm - to_start % lcm
print(res)
