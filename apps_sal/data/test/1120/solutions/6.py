a = int(input())
k = 0
while a > 0:
    a -= max([int(c) for c in str(a)])
    k += 1
print(k)
