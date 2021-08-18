
import collections


friends = collections.defaultdict(set)

m, k = list(map(int, input().split()))

for _ in range(m):
    a, b = list(map(int, input().split()))
    friends[a].add(b)
    friends[b].add(a)


for a in sorted(friends):
    a_friends = friends[a]
    probable_friends = []
    for b in friends:
        if a == b or b in a_friends:
            continue
        common_friends = a_friends & friends[b]
        if 100 * len(common_friends) // len(a_friends) >= k:
            probable_friends.append(b)
    print("%d:" % a, len(probable_friends), " ".join(map(str, sorted(probable_friends))))
