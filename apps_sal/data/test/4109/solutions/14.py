from collections import deque
from copy import deepcopy
(n, m, x) = list(map(int, input().split()))
books = [tuple(map(int, input().split())) for _ in range(n)]
D = deque()
D.append((-1, 0, [0 for _ in range(m)]))
ans = 10 ** 9
while D:
    (num, money, skill) = D.popleft()
    if num == n - 1:
        if all((s >= x for s in skill)):
            ans = min(ans, money)
    else:
        num += 1
        D.append((num, money, skill))
        book = books[num]
        skill = deepcopy(skill)
        money += book[0]
        for (i, b) in enumerate(book[1:]):
            skill[i] += b
        D.append((num, money, skill))
print(ans if ans != 10 ** 9 else -1)
