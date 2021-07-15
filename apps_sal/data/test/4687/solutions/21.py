N, K = map(int, input().split())
a = []
b = []
Sum = 0
for i in range(N):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
s = [*range(len(a))]
sort_s = sorted(s, key = lambda i: a[i])
sort_a = [a[i] for i in sort_s]
sort_b = [b[i] for i in sort_s]
for i in range(N):
    Sum += sort_b[i]
    if Sum >= K:
        print(sort_a[i])
        break
