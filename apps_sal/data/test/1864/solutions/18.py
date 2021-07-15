n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
if min(a)!=1:
    print(1)
else:
    print(-1)
