t = int(input())
for _ in range(t):
    a, b, c, d = [int(i) for i in input().split(" ")]
    sgn = (a + b) % 2
    small = False
    large = False
    if a == 0 and d == 0:
        small = True
    if b == 0 and c == 0:
        large = True
    okay = [True] * 4
    if sgn == 0:
        okay[0] = False
        okay[1] = False
    else:
        okay[2] = False
        okay[3] = False
    if small:
        okay[0] = False
        okay[3] = False
    if large:
        okay[1] = False
        okay[2] = False
    print(" ".join(["Ya" if okay[i] else "Tidak" for i in range(4)]))
