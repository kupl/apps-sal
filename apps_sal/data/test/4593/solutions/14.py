x = int(input())
a = 1
for i in range(2, x + 1):
    for j in range(1, x + 1):
        if j ** i <= x:
            a = max(a, j ** i)
        else:
            break
print(a)
