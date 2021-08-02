n, m = list(map(int, input().split()))
for i in range(m):
    good = 0
    morty = set()
    rick = set()
    now = list(map(int, input().split()))[1:]
    for c in now:
        if c < 0:
            morty.add(abs(c))
            if abs(c) in rick:
                good = 1
        if c > 0:
            rick.add(abs(c))
            if abs(c) in morty:
                good = 1
    if not good:
        print("YES")
        return
print("NO")
