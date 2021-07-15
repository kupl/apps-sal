q = int(input())
for _ in range(q):
    n = int(input())
    desks = list(map(int, input().split()))
    desks.sort(reverse=True)
    max_square = 1
    for i in range(n):
        if (i + 1) > max_square and desks[i] >= (i + 1):
            max_square = i + 1
    print(max_square)

