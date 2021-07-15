n = int(input())
num = 9
while len(str(n)) != 1:
    num += 1
    n += 1
    while n % 10 == 0:
        n //= 10
    
print(num)

