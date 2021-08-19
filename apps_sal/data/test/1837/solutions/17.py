n = int(input())
a = list(map(int, input().split()))
b = 0
c = 0
for (i, j) in enumerate(a):
    if i == j:
        b += 1
    elif a[j] == i:
        c = 2
    elif c == 0:
        c = 1
print(b + c)
