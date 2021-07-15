n = int(input())
a = [0] * 10 ** 6
b = []
for i in range(n):
    q, w = map(int, input().split())
    a[q] += 1
    b.append(w)
for i in range(n):
    print(n - 1 + a[b[i]], n - 1 - a[b[i]])
