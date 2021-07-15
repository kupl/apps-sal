def reverse(num):
    sum1 = 0
    while (num > 0):
        remainder = num % 10
        sum1 = remainder+sum1
        num = num // 10
    return sum1

n,a,b = list(map(int,input().split()))
c = 0
for i in range(1,n+1):
    if reverse(i)>=a and reverse(i)<=b:
        c+=i
print(c)
