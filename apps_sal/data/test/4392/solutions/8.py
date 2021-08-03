t = int(input())

for _ in range(t):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    p = list(sorted([int(x) for x in input().split()]))

    for _ in range(n + 2):
        for pos in p:
            if a[pos - 1] > a[pos]:
                a[pos - 1], a[pos] = a[pos], a[pos - 1]

    if a == list(sorted(a)):
        print("YES")
    else:
        print("NO")
