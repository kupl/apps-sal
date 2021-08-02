n, k = map(int, input().split())
people = {}
tmp = set()
for i in range(n):
    a, b = map(int, input().split())
    if people.get(a) == None:
        people[a] = []
    if people.get(b) == None:
        people[b] = []
    people[a].append(b)
    people[b].append(a)
    tmp.add(a)
    tmp.add(b)
tmp = sorted(tmp)
for i in tmp:
    ans = []
    print(str(i) + ': ', end='')
    for j in tmp:
        if i == j or people[i].count(j) != 0:
            continue
        cnt = 0
        for fr in people[j]:
            if people[i].count(fr) != 0:
                cnt += 1
        per = (100 * cnt) / len(people[i])
        if int(per) >= k:
            ans.append(j)
    print(len(ans), end=' ')
    for q in ans:
        print(q, end=' ')
    print()
