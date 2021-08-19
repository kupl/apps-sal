(i, f) = map(int, input().split())
(t, d) = map(int, input().split())
a = []
b = []
a = [i + j * d for j in range(t)]
b = [f + j * d for j in range(t)]
b.reverse()
for j in range(t):
    if a[j] >= b[j]:
        print(sum(a[:j]) + sum(b[j:]))
        quit()
