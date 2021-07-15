t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    diag = False
    for _ in range(n):
        a, b = map(int, input().split())
        c, d = map(int, input().split())
        if b == c:
            diag = True
    if m % 2 == 1:
        print("NO")
    else:
        print("YES" if diag else "NO")
