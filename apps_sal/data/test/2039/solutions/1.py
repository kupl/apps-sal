a = int(input())
x = list(map(int, input().split()))
n = 0
for i in range(1, a - 1):
    if x[i - 1] < x[i] and x[i] > x[i + 1]:
        n += 1
    if x[i - 1] > x[i] and x[i] < x[i + 1]:
        n += 1
print(n)
