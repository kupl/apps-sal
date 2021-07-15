from collections import deque


def calc_dist(head, my_dict, dist_a):
    deq = deque()
    deq.append((head, 0))
    visited = set()
    visited.add(head)

    while deq:
        ptr, length = deq.pop()
        dist_a[ptr] = length
        for item in my_dict[ptr]:
            if item not in visited:
                visited.add(item)
                deq.append((item, length+1))


n, u, v = list(map(int, input().split()))
my_dict = dict()

for i in range(n-1):
    a, b = list(map(int, input().split()))
    if a in my_dict:
        my_dict[a].append(b)
    else:
        my_dict[a] = [b]
    if b in my_dict:
        my_dict[b].append(a)
    else:
        my_dict[b] = [a]

dist_a = dict()
dist_b = dict()

calc_dist(u, my_dict, dist_a)
calc_dist(v, my_dict, dist_b)
ret = 0

for i in range(1, n+1):
    if dist_a[i] > dist_b[i]:
        continue
    else:
        ret = max(ret, dist_b[i] - 1)

print(ret)

