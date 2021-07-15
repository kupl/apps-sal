n, m = list(map(int, input().split()))

seen = set()
for a in map(int, input().split()):
    new = set()
    for b in seen:
        new.add((a+b) % m)
    seen |= new
    seen.add(a % m)
    if 0 in seen:
        print('YES')
        break
else:
    print('NO')

