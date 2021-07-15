mod = 1000000007
_ = input()
numbers = list(map(int,input().split()))
b = 2
flag = 1 if len(list([x for x in numbers if x%2 == 0])) else -1
for num in numbers:
    b = pow(b,num,mod)

b = b*pow(2,mod-2,mod)%mod # b = 2^n-1
a = (b+flag)*pow(3,mod-2,mod)%mod #a = (2^n-1 -/+ 1) / 3
print("%d/%d"%(a,b))


