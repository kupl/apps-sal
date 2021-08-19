(k, x) = map(int, input().split())
a = []
for i in range(x - k + 1, x + k):
    a.append(str(i))
print(' '.join(a))
