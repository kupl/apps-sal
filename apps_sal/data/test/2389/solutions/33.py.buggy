n, a, b, c = map(int, input().split())
s = [input() for _ in range(n)]
abc = [a, b, c]
d = {'A': 0, 'B': 1, 'C': 2}
dr = {0: 'A', 1: 'B', 2: 'C'}
ans = []
for i, x in enumerate(s):
    x = [d[y] for y in list(x)]
    if abc[x[0]] == abc[x[1]] == 1 and i < n - 1:
        nx = [d[y] for y in list(s[i + 1])]
        for j, y in enumerate(x):
            if y in nx:
                abc[y] += 1
                abc[x[(j + 1) % 2]] -= 1
                ans.append(dr[y])
                break
    elif abc[x[0]] > abc[x[1]]:
        abc[x[1]] += 1
        abc[x[0]] -= 1
        ans.append(dr[x[1]])
    else:
        abc[x[0]] += 1
        abc[x[1]] -= 1
        ans.append(dr[x[0]])
    for y in abc:
        if y < 0:
            print('No')
            return

print('Yes')
print(*ans, sep='\n')
