q = int(input())
for i in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    b = [-1 for i in range(n)]
    c = [0 for i in range(n + 2)]
    used = [True for i in range(n)]
    for i in range(n):
        if used[i]:
            d = a[i] - 1
            cell = a[i] - 1
            b[cell] = d
            c[d] += 1
            used[cell] = False
            while cell != i:
                cell = a[cell] - 1
                c[d] += 1
                b[cell] = d
                used[cell] = False
    for i in range(n):
        print(c[b[i]], end=" ")
    print()
