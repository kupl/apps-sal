h, w = list(map(int, input().split()))
table = [list(input()) for _ in range(h)]
table2 = []
for t in table:
    if t != ["."] * w:
        table2.append(t)
table2 = list(zip(*table2))
table3 = []
for t in table2:
    if list(t) != ["."] * len(t):
        table3.append(t)
table3 = list(zip(*table3))
for t in table3:
    print(("".join(t)))
