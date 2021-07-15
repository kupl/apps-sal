def reverse(num):
    test_num = 0
    while (num > 0):
        remainder = num % 10
        test_num = (test_num * 10) + remainder
        num = num // 10
    return test_num

a,b = list(map(int,input().split()))
c = 0
for i in range(a,b+1):
    if i == reverse(i):
        c+=1
print(c)
