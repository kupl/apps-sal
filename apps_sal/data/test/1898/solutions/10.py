n = int(input())
a = "I hate it"
b = "I love it"
c = "I hate that "
d = "I love that "
if n==1:
    print(a)
    return
ans = ""
for i in range(1,n+1):
    if i%2==1:
        ans+= c
    else:
        ans+= d

ans = ans[:-5]
ans += "it"
print(ans)

