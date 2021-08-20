from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    (*a,) = map(int, input().split())
    ca = Counter(a)
    if n % 2:
        print('Second')
        continue
    first = 0
    for ai in ca:
        if ca[ai] % 2:
            first = 1
            break
    if first:
        print('First')
    else:
        print('Second')
