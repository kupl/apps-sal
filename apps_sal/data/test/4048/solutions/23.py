n = int(input())

a = int(n**(1/2))
while True:
    if n % a == 0:
        print(a-1 + (n//a)-1)
        return
    a -= 1
