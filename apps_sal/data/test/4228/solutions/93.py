(N, L) = map(int, input().split())
a = []
for i in range(1, N + 1):
    a.append(L + i - 1)
b = []
for i in a:
    b.append(abs(i))
for i in range(1, N + 1):
    if abs(L + i - 1) == min(b):
        print(sum(a) - L - i + 1)
