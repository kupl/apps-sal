def main():
    n = int(input())
    pl, cl = 0, 0
    correct = True
    for i in range(n):
        p, c = list(map(int, input().split()))
        if c - cl > p - pl:
            correct = False
        if c < cl:
            correct = False
        if p < pl:
            correct = False
        pl, cl = p, c

    if correct:
        print("YES")
    else:
        print("NO")


t = int(input())
for _ in range(t):
    main()
