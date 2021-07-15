def f(n):
    if n % 400 == 0:
        return True
    elif n % 100 == 0:
        return False
    elif n % 4 == 0:
        return True
    else:
        return False
n = int(input())
N = n
c = 0
while True:
    n += 1
    if f(n):
        c += 2
    else:
        c += 1
    if c % 7 == 0 and f(n) == f(N):
        break
print(n)
    

