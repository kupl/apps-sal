n,k = list(map(int, input().split()))
tot = sum(map(int,input().split()))

i = 0
while(tot*2 < (k*2-1)*(n+i)):
    i+=1
    tot += k

print(i)

