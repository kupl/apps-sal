n = int(input())
l = list(map(int, input().split()))
k = 0
for i in range(2, n):
    if (l[i - 2] == 1 and l[i] == 1 and l[i - 1] == 0):
        l[i] = 0
        k += 1
print(k)
