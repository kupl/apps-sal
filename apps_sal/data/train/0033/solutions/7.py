import sys
input = sys.stdin.readline
inp, ip = lambda: int(input()), lambda: [int(w) for w in input().split()]

for _ in range(inp()):
    n = inp()
    prev = n
    print(2)
    for i in range(n - 1, 0, -1):
        print(i, prev)
        prev = (i + prev - 1) // 2 + 1
