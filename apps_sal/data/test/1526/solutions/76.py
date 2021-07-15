d=sorted(list(map(int,input().split())))
if d[0]%2==d[1]%2==d[2]%2:
    print(int((2*d[2]-d[1]-d[0])/2))
elif d[0]%2==d[1]%2:
    print(int((2*d[2]-d[1]-d[0])/2))
else:
    print(int((2*d[2]-d[0]-d[1]+1)/2)+1)
