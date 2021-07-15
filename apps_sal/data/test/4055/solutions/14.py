n = int(input())
a = list(map(int, input().split()))
num = 0
for i in range(2, n):
    if a[i] == 1 and a[i - 1] == 0 and a[i - 2] == 1:
        a[i] = 0
        num += 1

print(num)
