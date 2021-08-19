(m, k) = list(map(int, input().split()))
idd = set()
friends = dict()
for i in range(m):
    (f, s) = list(map(int, input().split()))
    idd.add(f)
    idd.add(s)
    if f not in list(friends.keys()):
        friends[f] = set()
    if s not in list(friends.keys()):
        friends[s] = set()
    friends[f].add(s)
    friends[s].add(f)
people = list(idd)
people.sort()
ans = dict()
for i in range(len(people)):
    ans[people[i]] = []
for i in range(len(people)):
    for j in range(len(people)):
        if i == j:
            continue
        if people[j] in friends[people[i]]:
            continue
        common = 0
        for fr in friends[people[j]]:
            if fr in friends[people[i]]:
                common += 1
        if common * 100 >= k * len(friends[people[i]]):
            ans[people[i]].append(people[j])
for i in range(len(people)):
    print(str(people[i]) + ': ' + str(len(ans[people[i]])) + ' ' + ' '.join(list(map(str, ans[people[i]]))))
