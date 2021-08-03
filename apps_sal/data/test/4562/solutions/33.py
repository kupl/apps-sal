n = int(input())
for i in range(1, 10**5 + 2):
    if i**2 > n:
        print(((i - 1)**2))
        return
