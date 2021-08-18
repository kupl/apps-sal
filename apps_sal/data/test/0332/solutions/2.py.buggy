from collections import defaultdict
n, m = map(int, input().split())
# rows and columns
# max 500

diag_a = defaultdict(list)
diag_b = defaultdict(list)

for x in range(n):
    for i, val in enumerate(list(map(int, input().split()))):
        diag_a[x + i].append(val)

for x in range(n):
    for i, val in enumerate(list(map(int, input().split()))):
        diag_b[x + i].append(val)

diag_a = {k: sorted(v) for k, v in diag_a.items()}
diag_b = {k: sorted(v) for k, v in diag_b.items()}
for k in diag_a.keys():
    if diag_a[k] != diag_b[k]:
        print("NO")
        return
print("YES")
