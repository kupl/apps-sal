def isPrime(n):
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,n,2):
        if i*i>n:
            break
        if n%i==0:
            return False
    return True
n=int(input())
if isPrime(n):
    print(1)
    print(n)
elif isPrime(n-2):
    print(2)
    print('2 '+str(n-2))
else:
    print(3)
    for i in range(2,n-3):
        if i>2 and i%2==0:
            continue
        if n-3-i<i:
            break
        if isPrime(i) and isPrime(n-3-i):
            print('3 '+str(i)+' '+str(n-3-i))
            break
