(numberOfcities, nBlocked) = [int(item) for item in input().split()]
blocked = set()
for i in range(nBlocked):
    (n, m) = [int(item) for item in input().split()]
    blocked.add(n)
    blocked.add(m)
point = 0
for k in range(1, numberOfcities + 1):
    if k not in blocked:
        point = k
        break
print(numberOfcities - 1)
for k in range(1, numberOfcities + 1):
    if k != point:
        print(point, k)
