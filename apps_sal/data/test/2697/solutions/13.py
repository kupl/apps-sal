n = int(input())
c = 0
for i in range(2, n + 1):
    f = 0
    for j in range(2, int(i**0.5) + 1):
        if(i % j == 0):
            f = 1
            break
    if(f == 0):
        c = c + 1
print(c)
