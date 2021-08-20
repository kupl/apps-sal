import sys
input = sys.stdin.readline
for f in range(int(input())):
    (n, r) = map(int, input().split())
    if r < n:
        print(r * (r + 1) // 2)
    else:
        sol = (n - 1) * n // 2
        sol += 1
        print(sol)
