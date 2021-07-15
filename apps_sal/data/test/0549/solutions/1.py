n = int(input())

a = 1
b = n

for i in range(2, int(n**.5)+1):
    if n % i == 0:
        a = i
        b = n//i

print(a,b)

