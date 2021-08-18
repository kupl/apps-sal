from collections import defaultdict
n, m = list(map(int, input().split()))
# rows # columns
m1 = [list(input().split()) for _ in range(n)]
m2 = [list(input().split()) for _ in range(n)]

row_change = defaultdict(int)
col_change = defaultdict(int)
count_change = 0

for x in range(n):
    for y in range(m):
        if m1[x][y] != m2[x][y]:
            count_change += 1
            row_change[x] += 1
            col_change[y] += 1
if count_change % 2:
    print("No")
    return
if all(v % 2 == 0 for k, v in list(row_change.items())) and all(v % 2 == 0 for k, v in list(col_change.items())):
    print("Yes")
    return
print("No")
