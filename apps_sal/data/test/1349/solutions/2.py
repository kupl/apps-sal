

t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    taps = [int(x) for x in input().split()]
    result = 0
    for i in range(1, n + 1):
        best = n + 1
        for x in taps:
            best = min([best, abs(x - i)])
        result = max([result, best])
    print(result + 1)

