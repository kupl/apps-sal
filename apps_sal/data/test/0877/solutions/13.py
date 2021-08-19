(n, m) = map(int, input().split())
uv = []
for i in range(m):
    mapp = list(map(int, input().split()))
    mapp.sort()
    uv.append(mapp)
all_tasks = [1, n]
for s in uv:
    all_tasks = [max(all_tasks[0], s[0]), min(all_tasks[1], s[1])]
if all_tasks[1] - all_tasks[0] + 1 < 2:
    print(0)
else:
    print(all_tasks[1] - all_tasks[0])
