for _ in range(int(input())):
    (n, k) = [int(x) for x in input().split()]
    a = sorted([int(x) for x in input().split()])
    b = sorted([int(x) for x in input().split()], reverse=True)
    for i in range(k):
        if a[i] < b[i]:
            (a[i], b[i]) = (b[i], a[i])
    print(sum(a))
