n = int(input())
a = []
b = []
for _ in range(n) :
    x, y = list(map(int, input().split()))
    a.append(x)
    b.append(y)
a.sort()
b.sort()
print(n + sum(map(max, a, b)))

