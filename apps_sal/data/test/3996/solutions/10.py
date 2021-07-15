mod = 1000000007
input()
numbers = list(map(int, input().split()))
b = 2
flag = 1 if len(list(filter(lambda x : x % 2 == 0, numbers))) else -1
for num in numbers:
    b = pow(b, num, mod)
b = b * pow(2, mod - 2, mod) % mod
a = (b + flag) * pow(3, mod - 2, mod) % mod
print("%d/%d"%(a, b))
