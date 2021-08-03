n = int(input())
lst = list(map(int, input().split()))
m = 10 ** 10
for i in range(201):
    a = i - 100
    temp = 0
    for j in range(n):
        temp += ((lst[j] - a) ** 2)
    m = min(m, temp)
print(m)
