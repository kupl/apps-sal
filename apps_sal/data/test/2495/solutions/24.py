n = int(input())
a = list(map(int, input().split()))

cost = 0
sum = 0
for i in range(n):
    sum += a[i]
    if i % 2 == 0:
        if sum >= 1:
            pass
        else:
            cost += 1 - sum
            sum = 1
    else:
        if sum <= -1:
            pass
        else:
            cost += sum + 1
            sum = -1

kost = 0
kom = 0
for i in range(n):
    kom += a[i]
    if i % 2 != 0:
        if kom >= 1:
            pass
        else:
            kost += 1 - kom
            kom = 1
    else:
        if kom <= -1:
            pass
        else:
            kost += kom + 1
            kom = -1

print(min(cost, kost))
