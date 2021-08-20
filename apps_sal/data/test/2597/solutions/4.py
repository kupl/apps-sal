k = int(input())
for _ in range(k):
    n = int(input())
    a = sorted(map(int, input().split()), reverse=True)
    for (i, v) in enumerate(a, start=1):
        if v < i:
            print(i - 1)
            break
    else:
        print(n)
