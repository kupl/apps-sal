n,m,k = list(map(int, input().split()))
lst = list(map(int, input().split()))
for i,a in enumerate(sorted(lst, reverse = True)):
    if k >= m:
        print(i)
        return
    k += a -1
if k >= m:
    print(n)
else:
    print(-1)

