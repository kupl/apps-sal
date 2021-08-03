n = int(input())
d = {}
for i in range(n):
    val = int(input())
    if val in list(d.keys()):
        d[val] += 1
    else:
        d[val] = 1
for i in list(d.keys()):
    for j in list(d.keys()):
        if i == j:
            continue
        if d[i] == d[j]:
            if d[i] + d[j] == n:
                print('YES')
                print(i, j)
                quit()
print('NO')
