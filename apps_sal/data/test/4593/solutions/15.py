X = int(input())
n = 1
if X<=3:
    print(1)
elif X==4:
    print(4)
else:
    n = 4
    for i in range(2,int(X**0.5)+1):
        b = i
        k = 1
        while b**k<=X:
            k += 1
        k -= 1
        if k>=2:
            n = max(n,b**k)
    print(n)
