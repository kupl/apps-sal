
a = int(input())
max_n = 0
max_1 = 0
max_2 = 0
k = 0
b = [int(i) for i in input().split()]
for i in range(len(b)):
    if max(b[i], max_n) > max_n:
        max_1 = max_n
        k = i + 1
        max_n = max(b[i], max_n)
dp = [i for i in range(len(b))]
dp.reverse()
max_n = 0
for i in dp:
    if max(b[i], max_n) > max_n:
        max_2 = max_n
        k = i + 1
        max_n = max(b[i], max_n)
print(str(k) + " " + str(max(max_1, max_2)))

