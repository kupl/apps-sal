n=int(input())
k=1
for i in range(2,n+1):
    k *= i
    k %= (10**9)+7
print(k)
