from fractions import gcd
def lcm(a, b):
    return (a // gcd(a, b)) * b
    
n, k = map(int, input().split())
if k == 1:
    print("Yes")
    return
n1 = 1
for i in range(1, k + 1):
    n1 = lcm(n1, i)
    if n % n1 != n1 - 1:
        print("No")
        return
if n % n1 == n1 - 1:
    print("Yes")
    return
print("No")
