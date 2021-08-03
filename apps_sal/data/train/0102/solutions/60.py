q = int(input())
for _ in range(q):
    n = int(input())
    t = (len(str(n)) - 1) * 9
    for i in range(1, 10):
        if int(str(i) * len(str(n))) <= n:
            t += 1
    print(t)
