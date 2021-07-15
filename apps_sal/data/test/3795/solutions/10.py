def gcd(x,y):
    if(y==0):
        return x
    return gcd(y,x%y)
 
 
n = int(input())
d = int(input())
e = int(input())
e*= 5
if(n > 10*e*d):
    print(n % gcd(e,d))
    return
 
ans = [0]
 
for i in range(1, n + 1):
    ans.append(i)
    if(i >= d):
        ans[i] = min(ans[i], ans[i - d])
    if(i >= e):
        ans[i] = min(ans[i], ans[i - e])
# print(ans)
print(ans[n])
