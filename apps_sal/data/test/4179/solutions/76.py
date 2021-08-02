n, m, c = map(int, input().split())

b = list(map(int, input().split()))
count = 0

for i in range(n):
    sum = 0
    a = list(map(int, input().split()))
    for j in range(len(b)):
        sum = sum + b[j] * a[j]
    sum = sum + c
    if sum > 0:
        count = count + 1

print(count)
