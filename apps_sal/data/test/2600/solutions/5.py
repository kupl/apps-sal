import sys
input = sys.stdin.readline
for f in range(int(input())):
    (n, m) = map(int, input().split())
    ones = [0] * ((n + m) // 2)
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(m):
            x = i + j
            if x > (n + m - 2) // 2:
                x = n + m - 2 - x
            if line[j] == 1:
                ones[x] += 1
    sol = 0
    for i in range((n + m - 1) // 2):
        tot = 2 * min(i + 1, n, m)
        sol += min(ones[i], tot - ones[i])
    print(sol)
