n = int(input())
A = [int(i) for i in input().split()]
m = int(input())
period = []
for _ in range(m):
    period.append([int(i) for i in input().split()])

total = sum(A)
time = -1
for p in period:
    if total <= p[0]:
        time = p[0]
        break
    if total >= p[0] and total <= p[1]:
        time = total
        break
print(time)

