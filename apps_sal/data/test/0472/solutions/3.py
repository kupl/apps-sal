def readln(): return tuple(map(int, input().split()))

n, = readln()
for s in range(1, 180):
    d = int((s**2 + 4 * n)**0.5)
    if d**2 == s**2 + 4 * n and (-s + d) % 2 == 0:
        x = (-s + d) // 2
        if sum(map(int, list(str(x)))) == s:
            import sys
            print(x)
            return
print(-1)

