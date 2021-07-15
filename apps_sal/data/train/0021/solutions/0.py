t = int(input())

for _ in range(t):
    n = list(input().strip())
    s = list(map(int, input().strip().split()))

    check = set(s)
    found = False
    for i in range(1, 1025):
        newset = set([e^i for e in s])
        if check == newset:
            print(i)
            found = True
            break
    if not found:
        print(-1)

