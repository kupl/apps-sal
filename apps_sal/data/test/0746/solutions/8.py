def S(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


(a, b) = list(map(int, input().split()))
mas = []
for i in range(int(input())):
    (x, y, v) = list(map(int, input().split()))
    mas.append(S(a, b, x, y) / v)
print(min(mas))
