n, A = map(int, input().split())
d = [int(x) for x in input().split()]
x = sum(d)
b = []

for i in range(n):
    b.append(d[i] - min(d[i], A - n + 1) + max(A - x + d[i], 1) - 1)
print(''.join([str(b[i]) + ' ' for i in range(n)]))
