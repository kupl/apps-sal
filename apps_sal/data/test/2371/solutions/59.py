n,z,w=list(map(int,input().split()))
a=list(map(int,input().split()))
a.insert(0,a[0])

print((max(abs(w-a[-1]),abs(a[-1]-a[-2]))))

