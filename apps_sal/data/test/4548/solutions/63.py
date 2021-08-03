n, m, x = map(int, input().split())
a = list(map(int, input().split()))
mas = [0] * (n + 1)
for i in a:
    mas[i] = 1
print(min(sum(mas[0:x]), sum(mas[x:n + 1])))
