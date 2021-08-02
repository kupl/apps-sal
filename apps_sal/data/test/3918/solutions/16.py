import heapq

n, k1, k2 = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

err = [abs(x - y) for x, y in zip(a, b)]

if k1 + k2 >= sum(err):
    print((k1 + k2 - sum(err)) % 2)

else:

    moves = k1 + k2
    err = [-a for a in err]
    heapq.heapify(err)

    while moves:
        x = heapq.heappop(err)
        x += 1
        heapq.heappush(err, x)
        moves -= 1

    print(sum([x**2 for x in err]))
