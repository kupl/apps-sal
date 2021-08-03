n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
mas = [0 for i in range(n)]
t = 0
for i in range(1, n, 2):
    mas[i] = l[t]
    t += 1
for i in range(0, n, 2):
    mas[i] = l[t]
    t += 1
print(*mas)
