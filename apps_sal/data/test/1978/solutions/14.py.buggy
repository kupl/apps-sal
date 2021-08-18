import sys
input = sys.stdin.readline

INF = 10**12
n = int(input())
edge = [[] for _ in range(n)]
for i in range(n):
    line = input().rstrip()
    for j, ch in enumerate(line):
        if i == j:
            edge[i].append(0)
        elif ch == "1":
            edge[i].append(1)
        else:
            edge[i].append(INF)
m = int(input())
a = [int(item) for item in input().split()]

if m == 2:
    print(2)
    print(" ".join([str(item) for item in a]))
    return

for k in range(n):
    for i in range(n):
        for j in range(n):
            edge[i][j] = min(edge[i][j], edge[i][k] + edge[k][j])

# for line in edge:
#     print(line)

frm_id = 0
mid_id = 1
to_id = 2
ans_num = 0
ans = [a[frm_id]]
ans_num += 1
while to_id < len(a):
    frm = a[frm_id] - 1
    mid = a[mid_id] - 1
    to = a[to_id] - 1
    if frm == to or not edge[frm][mid] + edge[mid][to] == edge[frm][to]:
        ans.append(mid + 1)
        ans_num += 1
        frm_id = mid_id
        to_id += 1
        mid_id += 1
    else:
        to_id += 1
        mid_id += 1
ans.append(to + 1)
ans_num += 1
print(ans_num)
print(" ".join([str(item) for item in ans]))
