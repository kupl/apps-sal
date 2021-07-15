n = int(input())
a = []
for i in range(n):
    a.append([int(x) - 1 for x in input().split()])
d1 = [0] * 2000
d2 = [0] * 2000
for i in a:
    d1[i[0] - i[1]] += 1
    d2[i[0] + i[1]] += 1
summ = 0
for i in range(2000):
    summ += d1[i] * (d1[i] - 1) // 2
    summ += d2[i] * (d2[i] - 1) // 2
print(summ)
