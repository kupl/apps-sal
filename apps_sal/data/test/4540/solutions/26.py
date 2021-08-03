n = int(input())

a = [int(i) for i in input().split()]
a.append(0)
a.insert(0, 0)

cost = 0
for i in range(1, len(a)):
    cost += abs(a[i - 1] - a[i])

for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] < a[i + 1]:
        ans = cost
    elif a[i - 1] > a[i] > a[i + 1]:
        ans = cost
    else:
        ans = cost - abs(a[i - 1] - a[i]) - abs(a[i] - a[i + 1]) + abs(a[i - 1] - a[i + 1])
    print(ans)
