t = int(input())
for i in range(t):
    n = int(input())
    s = input().split(' ')
    a = []
    for c in s:
        a.append(int(c))
    a.reverse()
    for i in range(n):
        if i % 2 == 0:
            a[i] = -a[i]
    for i in range(n):
        print(a[i], end=' ')
    print()
