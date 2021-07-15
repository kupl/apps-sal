n,k=map(int,input().split())
total=[]

while True:
    if n>=k:
        total.append((n%k))
        n=n//k
    if n<k:
        total.append((n))
        break
print(len(total))
