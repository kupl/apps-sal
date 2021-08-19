(n, k) = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
a = sorted(a, key=lambda x: x[0])
x = 0
for i in a:
    x += i[1]
    if x >= k:
        break
print(i[0])
