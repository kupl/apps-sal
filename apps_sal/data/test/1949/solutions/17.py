(n, m) = list(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))
b = list(set(a))
b.sort()
k = 0
for i in range(m):
    if i >= len(b):
        print(0)
    else:
        print(b[i] - k)
        k += b[i] - k
