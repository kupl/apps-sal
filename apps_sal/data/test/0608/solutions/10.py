n = int(input())
a = [int(i) for i in input().split()]
x = 0
p = 0
for i in range(n):
    if a[i] >= 4:
        x += 1
        if x == 3:
            p += 1
            x = 0
    else:
        x = 0
print(p)
