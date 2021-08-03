n = int(input())

q = list(map(int, input().split()))

p = [0]
for diff in q:
    p.append(p[-1] + diff)

lowest = min(p)
mod = 1 - lowest

a = [x + mod for x in p]

if sorted(a) == list(range(1, n + 1)):
    print(*a)
else:
    print(-1)
