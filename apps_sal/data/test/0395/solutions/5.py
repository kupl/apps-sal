lst = list(map(int, input().split()))
sm = sum(lst)
for a in range(len(lst)):
    for b in range(len(lst)):
        for c in range(len(lst)):
            if len(set([a, b, c])) != 3: continue
            q = lst[a] + lst[b] + lst[c]
            if sm - q == q:
                print('YES')
                return

print('NO')

