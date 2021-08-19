from collections import defaultdict
(m, k) = map(int, input().split())
friendship = defaultdict(set)
for i in range(m):
    (a, b) = map(int, input().split())
    friendship[a].add(b)
    friendship[b].add(a)
result = {}
for (x, friends) in friendship.items():
    s = set()
    for y in friendship:
        if x != y and (not y in friends):
            count = 0
            for z in filter(lambda f: y in friendship[f], friends):
                count += 100.0
            if count / len(friends) >= k:
                s.add(y)
    result[x] = s
for (x, friends) in sorted(result.items()):
    print(x, len(friends), end=' ', sep=': ')
    print(' '.join(map(str, sorted(friends))))
