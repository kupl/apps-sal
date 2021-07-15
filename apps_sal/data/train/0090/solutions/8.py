t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    b = []
    for i in range(n):
        if l[i] == 0:
            b.append(a[i])
    b.sort()
    b.reverse()
    j = 0
    for i in range(n):
        if l[i] == 0:
            a[i] = b[j]
            j += 1
    print(*a)
