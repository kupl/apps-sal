n = int(input())
a = [0] * (n + 1)
f = 1
x = list(map(int, input().split()))
for i in range(1, len(x)):
    a[x[i]] = 1
y = list(map(int, input().split()))
for i in range(1, len(y)):
    a[y[i]] = 1
for i in range(1, n + 1):
    if not a[i]:
        f = 0
print('I become the guy.' if f else 'Oh, my keyboard!')
