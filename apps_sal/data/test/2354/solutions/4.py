import sys

n, q = list(map(int, sys.stdin.readline().split()))
h = -(-n * n // 2)
for i in range(q):
    x, y = list(map(int, sys.stdin.readline().split()))
    ans = ((x - 1) // 2) * n
    if (x + y) % 2 == 0:
        if x % 2 == 0:
            ans += -(-n // 2)
            ans += y // 2
        else:
            ans += (y + 1) // 2
    else:
        ans += h
        if x % 2 == 0:
            ans += n // 2
            ans += (y + 1) // 2
        else:
            ans += y // 2
    print(ans)
