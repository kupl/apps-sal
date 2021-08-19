from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2:
        print('Second')
        continue
    c = Counter(a)
    check = True
    for i in list(c.values()):
        if i % 2:
            check = False
            break
    if check:
        print('Second')
    else:
        print('First')
