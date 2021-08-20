from collections import Counter
t = int(input())
for _ in range(t):
    s = input()
    best = len(s) - max(Counter(s).values())
    longest = [[0 for _ in range(10)] for _ in range(10)]
    for c in s:
        ci = int(c)
        for j in range(10):
            if longest[ci][j] % 2 == 0:
                longest[ci][j] += 1
            if longest[j][ci] % 2:
                longest[j][ci] += 1
    best = min(best, len(s) - max((longest[i][j] - longest[i][j] % 2 for i in range(10) for j in range(10) if i != j)))
    print(best)
