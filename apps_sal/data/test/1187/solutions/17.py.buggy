n, m = input().split(' ')
n, m = int(n), int(m)

ch = [[] for i in range(n + 1)]

edges_by_order = []

for i in range(m):
    x, y = input().split(' ')
    x, y = int(x), int(y)
    ch[x].append(y)
    edges_by_order.append((x, y))

for i in range(n + 1):
    ch[i] = sorted(ch[i])

st = [0 for i in range(n + 1)]
end = [0 for i in range(n + 1)]

timestamp = 0
cycle_exists = False


def dfs(x):
    nonlocal ch, st, end, timestamp, cycle_exists

    timestamp += 1
    st[x] = timestamp

    for y in ch[x]:
        if st[y] == 0:
            dfs(y)
        else:
            if st[y] < st[x] and end[y] == 0:
                cycle_exists = True

    timestamp += 1
    end[x] = timestamp


for i in range(1, n + 1):
    if st[i] == 0:
        dfs(i)

if not cycle_exists:
    print(1)
    for i in range(m):
        print(1, end=' ')
    print('', end='\n')
else:
    print(2)
    for i in range(m):
        x = st[edges_by_order[i][0]]
        y = st[edges_by_order[i][1]]

        if x < y:
            print(1, end=' ')
        else:
            print(2, end=' ')
    print('', end='\n')
