n=int(input())
ans = n-1
for i in range(1,int(n**(0.5))+1):
        if n % i == 0:
                ans = min(ans,i+n//i-2)
        else:
          continue
print(ans)
