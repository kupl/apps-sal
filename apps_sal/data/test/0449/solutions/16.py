n = int(input())
a = [100,20,10,5, 1]
ans = 0
i = 0
while i < 5 and n > 0:
    if a[i] <= n:
        ans+=n//a[i]
        n %= a[i]
    else:
        i+=1
print(ans)
