n,k = map(int,input().split())
if n == 1:
    print(k)
    return
su = k
for i in range(n-1):
    su *= (k-1)
print(su)
