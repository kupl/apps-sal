N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
num = sum(a)
for i in range(N):
    if a[i] <= b[i]:
        b[i] = b[i] - a[i]
        a[i] = 0
        if a[i + 1] <= b[i]:
            a[i + 1] = 0
        elif a[i + 1] > b[i]:
            a[i + 1] = a[i + 1] - b[i]
    elif a[i] > b[i]:
        a[i] = a[i] - b[i]
# print(num,sum(a))
num = num - sum(a)
print(num)
