tv1 = -1
tv2 = -1
shows = []
for _ in range(int(input())):
    (l, r) = map(int, input().split())
    shows.append((l, r))
shows.sort(key=lambda x: x[0])
for (l, r) in shows:
    if tv1 < l:
        tv1 = r
    elif tv2 < l:
        tv2 = r
    else:
        print('NO')
        break
else:
    print('YES')
