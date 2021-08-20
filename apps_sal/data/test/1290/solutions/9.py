(n, m) = list(map(int, input().split()))
l = list(map(int, input().split()))
mas = []
for i in range(n):
    mas.append(0)
for i in l:
    mas[i - 1] += 1
print(min(mas))
