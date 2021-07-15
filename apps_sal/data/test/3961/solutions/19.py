n = int(input())
ls = list(map(int,input().split()))
ls1 = list([0]*n)
sum = 2
ls1[0] = 2 
mod = 1000000007
for i in range(1,n):
    ls1[i] = 2
    k = ls[i]
    k -= 1
    for j in range(k,i):
        ls1[i] += ls1[j]
        ls1[i] %= mod
    sum += ls1[i]
    sum %= mod
   # print(ls1[i])
print(sum)
