from sys import stdin
input = stdin.readline
n = int(input())
a = [int(i) for i in input().split()]
num_neg = 0
num_zero = 0
cost = 0
for i in range(n):
    if a[i] == 0:
        cost += 1
        num_zero += 1
    elif a[i] < 0:
        num_neg += 1
        cost += -1 - a[i]
    else:
        cost += a[i] - 1
if num_zero > 0:
    print(cost)
elif num_neg % 2 == 1:
    print(cost + 2)
else:
    print(cost)
