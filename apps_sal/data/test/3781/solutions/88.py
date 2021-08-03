t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2:
        print("Second")
        continue
    from collections import Counter
    c = Counter(a)
    for i, j in c.items():
        if j % 2:
            print("First")
            break
    else:
        print("Second")
