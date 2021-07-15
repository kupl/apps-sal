n,k,q = list(map(int, input().split(' ')))
fr_lvl = list(map(int, input().split(' ')))
lvl = {i + 1: fr_lvl[i] for i in range(len(fr_lvl))}
online = 0
top_six = []
out = []
for step in range(q):
    count = 0
    found = False
    query = input()
    if query[0] == '1':
        online += 1
        if online < k + 1:
            top_six.append(int(query[2:]))
            top_six = sorted(top_six, key = lambda x: lvl[x])
        if online >= k+ 1:
            if lvl[top_six[0]] < lvl[int(query[2:])]:
                top_six[0] = int(query[2:])
                top_six = sorted(top_six, key = lambda x: lvl[x])
    if query[0] == '2':
        out.append(int(query[2:]) in top_six and 'YES' or 'NO')
for i in out:
    print(i)
