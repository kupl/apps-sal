t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    if not "1" in s:
        print(n)
        continue

    first = s.index("1")

    poss1 = 2 * (n - first)

    last = s[::-1].index("1")
    poss2 = 2 * (n - last)

    print(max(poss1, poss2))
