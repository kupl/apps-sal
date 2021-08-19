from collections import Counter

# inf = open('input.txt', 'r')
# reader = (map(int, line.split()) for line in inf)

# t, = next(reader)
t = int(input())

for _ in range(t):
    #     n, = next(reader)
    #     a = list(next(reader))
    n = int(input())
    a = [int(x) for x in input().split()]
    prev = Counter()
    mn = n + 1
    for i, el in enumerate(a):
        if el in prev:
            mn = min(mn, i - prev[el] + 1)
        prev[el] = i
    print(mn if mn < n + 1 else -1)

# inf.close()
