a = int(input())
summ = 0
for i in range(a):
    p = [int(x) for x in input().split()]
    summ += (p[2] - p[0] + 1) * (p[3] - p[1] + 1)
print(summ)
