# Fast IO (be careful about bytestring, not on interactive)

# import os,io
# input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

n = int(input())
a = list(map(int,input().split()))

a.sort()
b = [0] * n
for i in range((n + 1) // 2 - 1):
    b[2 * i + 1] = a[i]
if n % 2 == 0:
    b[n - 1] = a[n // 2 - 1]
for i in range((n + 1) // 2 - n % 2 ,n):
    b[2 * i - 2 * ((n + 1) // 2 - n % 2)] = a[i]
cnt = 0
for i in range(n):
    if i > 0 and i < n-1 and b[i] < b[i - 1] and b[i] < b[i + 1]:
        cnt += 1 
print(cnt)
print(" ".join(map(str,b)))
