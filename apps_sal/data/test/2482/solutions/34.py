n, k, l = map(int, input().split())
load = [[] for _ in range(n)]
train = [[] for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    load[a].append(b)
    load[b].append(a)
for _ in range(l):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    train[a].append(b)
    train[b].append(a)

# 道路の連結グループ
load_grp_id = [-1] * n
not_grp = set(range(n))
while not_grp:
    t0 = not_grp.pop()
    todo = [t0]
    load_grp_id[t0] = t0
    while todo:
        t = todo.pop()
        l = load[t]
        for li in l:
            if load_grp_id[li] == -1:
                load_grp_id[li] = t0
                not_grp.discard(li)
                todo.append(li)
# 鉄道の連結グループ
train_grp_id = [-1] * n
not_grp = set(range(n))
while not_grp:
    t0 = not_grp.pop()
    todo = [t0]
    train_grp_id[t0] = t0
    while todo:
        t = todo.pop()
        l = train[t]
        for li in l:
            if train_grp_id[li] == -1:
                train_grp_id[li] = t0
                not_grp.discard(li)
                todo.append(li)

d = {}
for i in range(n):
    lid = load_grp_id[i]
    tid = train_grp_id[i]
    if (lid, tid) in d:
        d[(lid, tid)] += 1
    else:
        d[(lid, tid)] = 1
ans = []
for i in range(n):
    lid = load_grp_id[i]
    tid = train_grp_id[i]
    ans.append(str(d[(lid, tid)]))
print(' '.join(ans))
