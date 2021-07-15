import queue

n, m = list(map(int, input().split()))
am_bm = []
side_map = dict()
for i in range(m):
    ai, bi = list(map(int, input().split()))
    if ai not in side_map:
        side_map[ai] = set()
        side_map[ai].add(bi)
    else:
        side_map[ai].add(bi)
    if bi not in side_map:
        side_map[bi] = set()
        side_map[bi].add(ai)
    else:
        side_map[bi].add(ai)
    am_bm.append((ai, bi))

counter = 0
for i in range(m):
    a, b = am_bm[i]
    q = queue.Queue()
    q.put(1)
    node_passed = set()
    node_passed.add(1)
    while not q.empty():
        a_tmp = q.get()
        for b_tmp in side_map[a_tmp]:
            if a_tmp == a and b_tmp == b or a_tmp == b and b_tmp == a:
                pass
            elif b_tmp not in node_passed:
                q.put(b_tmp)
                node_passed.add(b_tmp)
    if len(node_passed) == n:
        counter += 1
print((m - counter))

