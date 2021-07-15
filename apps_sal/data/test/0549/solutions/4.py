n = int(input())
top = 0

for i in range(1, int(n**(1/2))+1):
    if n % i == 0:
        top = max((top, i))

print(top, n//top)

