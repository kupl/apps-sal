tests = int(input())
for test in range(tests):
    n = int(input())
    l = len(str(n))
    c = 0
    for i in range(1, l+1):
        for j in range(1, 10):
            a = int(str(j)*i)
            if a <= n:
                c += 1
    print(c)

