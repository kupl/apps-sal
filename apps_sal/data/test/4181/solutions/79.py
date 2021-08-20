n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
q = sum(a)
for i in range(n):
    if a[i] <= b[i]:
        a[i + 1] -= b[i] - a[i]
        a[i] = 0
        if a[i + 1] < 0:
            a[i + 1] = 0
    elif a[i] > b[i]:
        a[i] -= b[i]
print(q - sum(a))
