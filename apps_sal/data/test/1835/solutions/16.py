Q = int(input())
for q in range(Q):
    n = int(input())
    arr = [input() for i in range(n)]

    lens = [len(i) % 2 for i in arr]
    counts = [i.count('1') for i in arr]
    if sum(counts) % 2 == 0:
        print(n)
    else:
        if 1 in lens:
            print(n)
        else:
            print(n - 1)

