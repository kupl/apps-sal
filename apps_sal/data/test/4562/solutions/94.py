# ABC077B
n = int(input())
while n > 0:
    tmp = n**(1 / 2)
    if(tmp == int(tmp)):
        print(n)
        break
    n -= 1
