t = int(input())
for i in range(t):
    (n, r) = list(map(int, input().split()))
    l = list(map(int, input().split()))
    if r == 1:
        s = sum(l) % n
        if s == 0:
            s = n
        print(s)
    else:
        s = 2 * l[0] - r + 1 - sum(l)
        s = s % n
        if s == 0:
            s = n
        print(s)
