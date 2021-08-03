def ceil(a, b):
    if (a % b == 0):
        return a // b
    else:
        return a // b + 1


t = int(input())
for case in range(t):
    n, m, k = list(map(int, input().split()))
    taken = min(m, n // k)
    remaining = m - taken
    print(taken - ceil(remaining, k - 1))
