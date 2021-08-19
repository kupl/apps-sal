from collections import deque
(n, k) = list(map(int, input().split()))
ar = list(map(int, input().split()))
lol = deque([])
for elem in ar:
    if elem not in lol:
        if len(lol) == k:
            lol.pop()
        lol.appendleft(elem)
print(len(lol))
print(*lol)
