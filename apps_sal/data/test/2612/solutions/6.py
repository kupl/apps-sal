for f in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    poss = [1] * (n + 1)
    for i in range(1, n):
        j = 2
        while j * i <= n:
            if s[j * i - 1] > s[i - 1]:
                poss[i * j] = max(poss[i * j], poss[i] + 1)
            j += 1
    print(max(poss))
