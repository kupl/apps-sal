# solution
import io
from collections import Counter

nim, mike, kite, *AB = list(map(int, open(0).read().split()))

move = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),  (0, 0),  (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]

C = Counter()
for a, b in zip(*[iter(AB)] * 2):
    C.update(
        (a - i, b - j)
        for i, j in move
        if 2 <= a - i <= nim - 1 and 2 <= b - j <= mike - 1
    )

D = Counter(v for _, v in list(C.items()))

print(((nim - 2) * (mike - 2) - sum(D.values())))
for i in range(1, 10):
    print((D[i]))

