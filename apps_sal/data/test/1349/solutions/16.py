t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    x = [int(x)-1 for x in input().split()]

    b = [False] * n
    tn = 0

    while not all(b):
        tn += 1
        for i in x:
            for j in range(max(0, i - (tn - 1)), min(i + (tn - 1) + 1, n)):
                b[j] = True
    print(tn)

