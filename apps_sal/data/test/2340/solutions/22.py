q = int(input())

for _ in range(q):
    h, n = list(map(int, input().split()))

    p = list(map(int, input().split()))[1:]
    dangers = []

    rows = 1
    i = 0
    while i < len(p):
        if i > 0 and p[i] == p[i - 1] - 1:
            rows += 1
        else:
            rows = 1

        if (i == len(p) - 1 or p[i + 1] != p[i] - 1) and p[i] > 1:
            if rows % 2:
                dangers.append(p[i])
        #print(rows, i, p[i])
        i += 1
   
    print(len(dangers))

