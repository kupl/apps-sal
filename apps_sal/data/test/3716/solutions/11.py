n = int(input())
if n < 3: 
    print(n)
    return
if n % 2 != 0: 
    print(n*(n-1)*(n-2))
    return
if n % 3 == 0: 
    print((n - 3)* (n - 1) * (n - 2))
    return
print((n - 1) * (n) * (n - 3))

