t = int(input())
ns = list(map(int, input().split()))
for n in ns:
    a = [[1], [2], [4], [3]]
    for i in range(n - 1):
        d = a[0][-1] * 2 + 2
        a[0].append(d)
        d = a[1][-1] * 2 + 1
        a[1].append(d)
        d = a[2][-1] * 2 + 2
        a[2].append(d)
        d = a[3][-1] * 2
        a[3].append(d)
    for i in a:
        for j in i:
            print(j, end=' ')
        print()
