m=str(input())
z=int(input())

def pol(s):
    for i in range(int(len(s)/2)):
        if not(s[i]==s[len(s)-1-i]):
            return False
            break;
    return True

#pol(m)
l=len(m)

l1=int(l/z)
#print (l1)
start=0
end=l1
if ((len(m)<z) or (not(l%z)==0)):
    print("NO")
    return
for j in range(z):
    u=m[start:end]
    start+=l1
    end+=l1
    if (not(pol(u))):
        print("NO")
        return
print("YES")

