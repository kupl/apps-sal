n,m = map(int, input().split())
k = 0
for i in range(n):
    a = list(map (int, input().split()))
    for j in range(m):
        if a[j] == 1 and (j in [0, m-1] or i in [0, n-1]):
            k=1
           
if k == 1:
    print(2)
else:
    print(4)
