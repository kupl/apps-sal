n = int(input())
a = [int(i) for i in input().split()]
b = [(a[i], n - i) for i in range(n)]
b.sort(reverse=True)
b = [(b[i][0], n - b[i][1]) for i in range(n)]

m = int(input())
for qu in range(m):
    k, p = list(map(int, input().split()))
    c = b[:k]
    c.sort(key = lambda x: x[1])
    print(c[p-1][0])


