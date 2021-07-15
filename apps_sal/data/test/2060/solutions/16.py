def __starting_point():
    tc = int(input().strip())
    for _ in range(tc):
        x = int(input().strip())
        found = False
        for a in range(x):
            for b in range(x):
                if (3 * a) + (7 * b) == x:
                    found = True
                    break
            if found:
                break
        print("YES" if found else "NO")

__starting_point()
