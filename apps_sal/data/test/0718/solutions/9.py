s = input()
ans = 0
f = True
while f:
    s = str(int(s)+1)
    ans+=1
    for i in s:
        if i == '8':
            f = False
print(ans)
            

