n,k = map(int, input().split())
s = input()
t = 0
for item in s:
    if item == '#':
        t+=1
        if (t==k) :
            print("NO")
            return
    else:
        t=0
print("YES")
