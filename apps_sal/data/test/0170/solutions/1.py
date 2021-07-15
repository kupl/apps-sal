__author__ = 'Andrey'
import collections
import time
start = time.time()
n = int(input())
cards_1 = collections.deque(list(map(int, input().split()))[1:])
cards_2 = collections.deque(list(map(int, input().split()))[1:])
c = 0
bad = False
while cards_1 and cards_2:
    end = time.time()
    if end - start > 1.85:
        bad = True
        break
    n_1 = cards_1.popleft()
    n_2 = cards_2.popleft()
    c += 1
    if n_1 > n_2:
        cards_1.append(n_2)
        cards_1.append(n_1)
    else:
        cards_2.append(n_1)
        cards_2.append(n_2)
else:
    print(c, 1 if cards_1 else 2)
if bad:
    print(-1)

