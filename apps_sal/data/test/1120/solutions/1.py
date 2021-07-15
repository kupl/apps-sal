
n=int(input())
k=0

while n:
    n-=int(max(list(str(n))))
    k+=1

print(k)

