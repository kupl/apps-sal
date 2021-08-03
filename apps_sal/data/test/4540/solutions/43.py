n = int(input())
a = list(map(int, input().split()))

total = 0
for i in range(1, n):
    total += abs(a[i] - a[i - 1])

total += abs(a[0]) + abs(a[-1])

a.insert(0, 0)
a.append(0)
for i in range(1, n + 1):
    if a[i - 1] <= a[i] and a[i] <= a[i + 1]:
        print(total)
    elif a[i + 1] <= a[i] and a[i] <= a[i - 1]:
        print(total)
    elif max(a[i - 1], a[i + 1]) < a[i]:
        print(total - abs(a[i] - max(a[i - 1], a[i + 1])) * 2)
    elif a[i] < min(a[i - 1], a[i + 1]):
        print(total - abs(a[i] - min(a[i - 1], a[i + 1])) * 2)
