l,r=map(int,input().split())
print("YES")
for i in range(int((r-l+1)/2)):

    print(l,l+1)
    l+=2
