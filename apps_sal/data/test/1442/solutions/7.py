import operator

n, s = list(map(int, input().split()))
orders = []
for i in range(n):
    orders.append(tuple(map(str, input().split())))

aggr = {}
for order in orders:
    key = (order[0][0], int(order[1]))
    if key not in aggr:
        aggr[key] = 0
    aggr[key] += int(order[2])

books = {"B": [], "S": []}
for key in aggr:
    book = books[key[0]]
    volume = aggr[key]
    book.append((key[0], key[1], volume))


for k in books:
    books[k] = list(reversed(sorted(books[k], key=operator.itemgetter(1))))

lenB = len(books["S"])
for i in range(min(lenB, s)):
    order = books["S"][max(0, lenB - s) + i]
    print("S %d %d" % (order[1], order[2]))

for i in range(min(len(books["B"]), s)):
    order = books["B"][i]
    print("B %d %d" % (order[1], order[2]))
