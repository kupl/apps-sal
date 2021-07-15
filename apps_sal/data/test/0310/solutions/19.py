n, k = map(int, input().split())
q = 2 * n + 1
p = k // n
if k % n:
    print(p + 1)
else:
    print(p)
