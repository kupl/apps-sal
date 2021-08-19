n = int(input())
a = [int(i) for i in input().split()]
b = [0 for i in range(n)]
for (i, j) in enumerate(a):
    b[j - 1] = i
sum = 0
for i in range(1, n):
    sum += abs(b[i] - b[i - 1])
print(sum)
