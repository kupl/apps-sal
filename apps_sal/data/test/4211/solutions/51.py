n = int(input())
b = list(map(int, input().split()))
a = []
a.append(b[0])
for i in range(1, n - 1):
    a.append(min(b[i - 1], b[i]))
a.append(b[-1])
num = 0
for i in range(n):
    num += a[i]
print(num)
