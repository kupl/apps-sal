
n = int(input())
l = []

i = 2
while n!=1:
    if n%i==0:
        while n%i==0:
            n/=i
            l.append(str(i))
    else:
        i+=1

print("".join(l))

