n = int(input())
x = n
for i in range(1, 10):
    if(n % i == 0):
        x = n / i
if(x < 10):
    print("Yes")
else:
    print("No")
