n = int(input())
x = n
sum = 0
while x:
    sum += (x % 10)
    x //= 10
if(n % sum == 0):
    print("Yes")
else:
    print("No")

