import sys
from bisect import bisect
from collections import Counter, defaultdict

l1 = sys.stdin.readline()
l2 = sys.stdin.readline()

n, k = map(int, l1.split(' '))
books = list(map(int, l2.split(' ')))

cost = 0
cache = set()

x = defaultdict(list)
for i, book_id in enumerate(books):
    x[book_id].append(i)

for i, book_id in enumerate(books):
    if book_id in cache:
        continue

    if len(cache) < k:
        cache.add(book_id)
        cost += 1
        continue

    min_next_closest = i
    to_evict = next(iter(cache))
    for x_id in cache:
        indices = x[x_id]
        index = bisect(indices, i)
        if index == len(indices):
            to_evict = x_id
            break
        next_closect = indices[index]
        if next_closect > min_next_closest:
            min_next_closest = next_closect
            to_evict = x_id
    # print("To evict %s" % to_evict)
    cache.remove(to_evict)
    cache.add(book_id)
    cost += 1

print(cost)
