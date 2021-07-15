d,n =map(int,input().split())
if n%100 != 0:
    ans = 100**d*n
else:
    ans = 100**d*101
print(ans)
