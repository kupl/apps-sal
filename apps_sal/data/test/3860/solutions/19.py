b=int(input())
g=int(input())
n=int(input())
cnt=0
for i in range(n+1):
    if i<=b and (n-i)<=g:
        cnt += 1
print(cnt)
