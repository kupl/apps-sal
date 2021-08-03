n = int(input())
k = int(input())
x = int(input())
y = int(input())
cost = 0
if n > k:
    for i in range(k):
        cost += x

    for j in range(k, n):
        cost += y
    print(cost)

elif n <= k:
    for i in range(n):
        cost += x
    print(cost)
