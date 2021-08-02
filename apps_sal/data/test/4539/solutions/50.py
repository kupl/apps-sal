n = int(input())

N = n

sum = int(0)
while(n != 0):
    sum += n % 10
    n //= 10

if N % sum == 0:
    print("Yes")
else:
    print("No")
