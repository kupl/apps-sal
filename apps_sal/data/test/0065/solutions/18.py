n = int(input())
a = list(map(int, input().split()))
x = min(a)
length = n
ind = -1
for i in range(n):
    if a[i] == x and ind == -1:
        ind = i
    elif a[i] == x and ind >= 0:
        if i - ind < length:
            length = i - ind
        ind = i
print(length)
