n,k = map(int,input().split())
i = 1
while n // k >  0:
    n = n // k
    i += 1
print(i)
