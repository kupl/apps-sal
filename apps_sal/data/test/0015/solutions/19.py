
try:
    while True:
        a, b, c = list(map(int, input().split()))
        if c == 0:
            print("YES" if a == b else "NO")
        elif c > 0:
            print("YES" if b in range(a, int(1e10), c) else "NO")
        else:
            print("YES" if b in range(a, int(-1e10), c) else "NO")

except EOFError:
    pass
