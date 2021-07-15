n, c = map(int, input().split())
pr = list(map(int, input().split()))
maxim = 0
for cont in range(0,n-1,1):
    m = pr[cont]-pr[cont+1]-c
    if m > maxim:
        maxim = m
print(maxim)
