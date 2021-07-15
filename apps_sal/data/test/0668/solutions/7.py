n = int(input())
counts = list(map(int, input().split()))
ai = [-1] * n

if counts[0] > 0 and sum(counts) >= n - 1:
    print(n - 1)
    k = sum(counts) - n + 1
    ai[0] = counts[0]
    counts[0] = -1
    boolean = True
    while min(ai) == -1:
        j = 0
        boolean = False
        for j in range(n):
            while ai[j] > 0 and min(ai) == -1:
                i = counts.index(max(counts))
                ai[j] -= 1
                ai[i] = counts[i]
                counts[i] = -1
                print(j + 1, i + 1)

else:
    print(-1)
