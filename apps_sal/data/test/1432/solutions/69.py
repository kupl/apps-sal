n = int(input())
a = list(map(int, input().split()))
num = 0
for i in range(n):
    if i % 2 == 0:
        num = num + a[i]
    else:
        num = num - a[i]
k = num
for i in range(n):
    print(k, end=" ")
    k = 2 * a[i] - k
