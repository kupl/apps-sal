n = int(input())
a = list(map(int,input().split()))

k = 1

for i in range(n):
    k *= 2
    while a[i]%k == 0:
        k *= 2
    k //= 2
x = 0
for i in range(n):
    if a[i]%k == 0:
        #print(1,end=' ')
        x += 1
#print()
print(k,x)
