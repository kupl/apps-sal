from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
c = Counter(arr)
c = list(c.values())
c.sort()
s = n
sol = []
removed = 0
for k in range(1, n + 1):
    rest = k - removed
    while c and c[-1] > s // rest:
        s -= c[-1]
        c.pop()
        rest -= 1
        removed += 1
    sol.append(s // rest)
print('\n'.join(map(str, sol)))
