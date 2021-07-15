n=int(input())
a,b=map(int,input().split())
n_a=a//n
n_b=(b+n-1)//n
# print(n_a,n_b)
for i in range(n_a-1,n_b+1):
    if a<=n*i<=b:
        print("OK")
        return
print("NG")
