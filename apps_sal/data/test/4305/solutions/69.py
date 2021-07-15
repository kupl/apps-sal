h, a=list(map(int,input().split()))
if h%a == 0:
    count=h//a
else:
    count = h//a+1
print(count)

