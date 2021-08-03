t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    b = []
    if sum(l) < n:  # exist non-blocked
        for i in range(n):
            if l[i] == 0:
                b.append(a[i])
        b.sort(reverse=True)
        j = 0
        for i in range(n):
            if l[i] == 0:
                print(b[j], end=' ')
                j += 1
            else:
                print(a[i], end=' ')
        print()
    else:
        for i in range(n):
            print(a[i], end=' ')
        print()
