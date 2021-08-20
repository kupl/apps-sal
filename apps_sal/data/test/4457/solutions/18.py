n = int(input())
l = list(map(int, input().split()))
l1 = [i for i in range(1, n + 1)]
for i in range(n):
    min1 = i
    for j in range(i + 1, n):
        if l[j] > l[min1]:
            min1 = j
    (l[i], l[min1]) = (l[min1], l[i])
    (l1[i], l1[min1]) = (l1[min1], l1[i])
count = 0
for i in range(n):
    count += l[i] * i + 1
print(count)
print(*l1)
