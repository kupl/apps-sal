n = int(input())
a = list(map(int, input().split()))
num = 0
for i in range(n):
    if a[i] < 0:
        num += -1 * a[i]
    else:
        num += a[i]

print(num)
