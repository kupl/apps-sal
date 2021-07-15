n,m = list(map(int, input().split()))
a = input()
b = input()
if n > m:
    b = "0"*(n-m) + b
elif n < m:
    a = "0"*(m-n) + a
dem = 0
A = []
for i in range(max(n,m)):
    if b[i] == "1":
        dem += 1
    A.append(dem)
ans =0
pows = 1
for i in range(max(n,m)-1,-1,-1):
    if a[i] =="1":
        ans += pows*A[i]
    pows = (2*pows)%998244353
print(ans%998244353)

