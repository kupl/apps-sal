n = int(input())
sum = 0
for _ in range(n):
    sum += [float(i) for i in input().split(' ')][1]
print(5 + sum / n)
