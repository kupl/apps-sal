n = int(input())
works = {}
for _ in range(n):
    a, b = list(map(int, input().split()))
    if b not in works:
        works.setdefault(b, [a])
    else:
        works[b].append(a)
works = sorted(list(works.items()), key=lambda x: x[0])
total = 0
for key, value in works:
    total += sum(value)
    if total > key:
        print('No')
        break
else:
    print('Yes')
