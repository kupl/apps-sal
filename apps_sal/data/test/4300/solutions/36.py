a = int(input())
b = 0
c = list(map(int, input().split()))
for i in range(a):
    for k in range(a):
        b = b + c[i] * c[k]
for u in range(a):
    b = b - c[u] * c[u]
print(int(b / 2))
