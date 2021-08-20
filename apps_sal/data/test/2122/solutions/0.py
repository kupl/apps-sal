import sys
import heapq
from collections import namedtuple
Record = namedtuple('Record', ['index', 'book_id'])
l1 = sys.stdin.readline()
l2 = sys.stdin.readline()
(n, k) = list(map(int, l1.split(' ')))
books = list(map(int, l2.split(' ')))
cost = 0
cache = set()
prev = dict()
next = [n + 1] * n
inactive_ids = set()
book_to_record = dict()


def serve_book(book_id, i):
    cache.add(book_id)
    record = Record(-next[i], book_id)
    heapq.heappush(h, record)
    book_to_record[book_id] = record


h = []
for (i, book_id) in enumerate(books):
    if book_id in prev:
        next[prev[book_id]] = i
    prev[book_id] = i
for (i, book_id) in enumerate(books):
    if book_id in cache:
        previous_record = book_to_record[book_id]
        inactive_ids.add(id(previous_record))
        serve_book(book_id, i)
        continue
    if len(cache) < k:
        cost += 1
        serve_book(book_id, i)
        continue
    while True:
        item = heapq.heappop(h)
        if id(item) in inactive_ids:
            inactive_ids.remove(id(item))
            continue
        cache.remove(item.book_id)
        serve_book(book_id, i)
        cost += 1
        break
print(cost)
