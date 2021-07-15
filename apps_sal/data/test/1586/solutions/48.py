n = int(input())

if n%2==1:
    print((0))
    return

fcnt = 0
tmp = 5
while n>=tmp:
    fcnt+=(n//2)//tmp
    tmp*=5

print(fcnt)

