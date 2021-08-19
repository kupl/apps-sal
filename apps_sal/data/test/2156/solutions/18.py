n = int(input())
a = list(map(int, input().split(' ')))
q = int(input())
suma = [0]
t = 0
for i in range(n):
    t += a[i]
    suma.append(t)
for i in range(q):
    (l, r) = map(int, input().split(' '))
    temp = suma[r] - suma[l - 1]
    print(temp // 10)
