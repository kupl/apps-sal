(a, b, k) = map(int, input().split())
x = []
y = []
if b - a < k:
    k = b - a + 1
for i in range(a, a + k):
    x.append(i)
for i in range(b - k + 1, b + 1):
    x.append(i)
x = list(set(x))
x.sort()
for i in range(len(x)):
    print(x[i])
