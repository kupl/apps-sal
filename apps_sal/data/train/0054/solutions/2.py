q = int(input())
for i in range(q):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    s = 0
    for i in a:
        if i <= 2048:
            s += i
    print("YES" if s >= 2048 else "NO")

