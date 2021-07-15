k = int(input())
a = 0
b = 0
for i in range(1, k+1):
    if i%2 == 0:
        a += 1
    else:
        b += 1
print(a*b)
