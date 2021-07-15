def f(n):
    n+=1
    while n%10==0:
        n/=10
    return n

x = int(input())
l = [x]
while 1:
    x = f(x)
    if x in l:
        break
    l.append(x)
print(len(l))
