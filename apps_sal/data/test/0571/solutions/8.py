import sys
input = sys.stdin.readline

n=int(input())
s=list(input().strip())

if n%2==1:
    print(":(")
    return

if n==2:
    if s[0]==")" or s[1]=="(":
        print(":(")
        return

    else:
        print("()")
        return

if s[0]==")" or s[1]==")" or s[-1]=="(" or s[-2]=="(":
    print(":(")
    return

s[0]="("
s[1]="("
s[-1]=")"
s[-2]=")"

r=s.count("(")
l=s.count(")")
q=s.count("?")

x=(l-r+q)//2
y=(r-l+q)//2

if x<0 or y<0:
    print(":(")
    return
    
count=0
for i in range(n):
    if s[i]=="?":
        s[i]="("
        count+=1

    if count==x:
        break

for j in range(i,n):
    if s[j]=="?":
        s[j]=")"


NOW=1
for i in range(1,n-1):
    if s[i]=="(":
        NOW+=1
    else:
        NOW-=1

    if NOW==0:
        print(":(")
        return

print("".join(s))

        

