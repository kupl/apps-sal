from collections import defaultdict
import io

nim, mike = map(int, input().split())
kite = list(map(int, input().split()))
for i in range(nim):
    kite[i] -= mike
qwe = defaultdict(int)
qwe[0] = 1
for o in kite:
    for j, c in list(qwe.items()):
        qwe[j + o] += c
print(qwe[0] - 1)
