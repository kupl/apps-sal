n, a = list(map(int, input().split()))
b = []
t = 1

if a % 2 == 0:
    for i in range(2, n + 1, 2):
        b.append(i)
    b.reverse()
else:
    for i in range(1, n, 2):
        b.append(i)

i = 0
while b[i] != a:
    t += 1
    i += 1


print(t)
