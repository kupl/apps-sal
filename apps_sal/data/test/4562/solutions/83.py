n = int(input())
for i in range(1, n):
    if i**2 > n:
        print((i-1)**2)
        break
else:
    print(1)
