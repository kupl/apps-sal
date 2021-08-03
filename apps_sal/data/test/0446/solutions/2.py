
n = int(input())

for k in range(20, 0, -1):
    div = (2**k - 1) * (2**(k - 1))
    if n % div == 0:
        print(div)
        break
