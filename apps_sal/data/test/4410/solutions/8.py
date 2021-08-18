t = int(input())
for i in range(t):
    a, b = list(map(int, input().split()))
    D = list(input())

    sep = []
    c = b

    for j in range(a):
        if D[j] == '1':
            sep.append(max(0, c - b))
            c = 0
        else:
            c += 1

    sep.append(max(0, c))

    tot = 0
    for j in sep:
        tot += j // (b + 1)

    print(tot)
