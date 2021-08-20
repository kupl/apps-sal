n = int(input())
a = []
for i in range(n):
    (x, y) = map(int, input().split())
    a.append(y)
p = int(input())
for i in range(n):
    if p <= a[i]:
        print(n - i)
        break
