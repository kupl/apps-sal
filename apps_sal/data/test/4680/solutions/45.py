a,b,c = input().split()

if (a+b+c).count('5')==2 and (a+b+c).count('7') ==1:
    print("YES")
else:
    print("NO")

