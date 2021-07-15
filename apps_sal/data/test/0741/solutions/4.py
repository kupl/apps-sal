n,m =list(map(int, input().split() ) )
a=list(map(int, input().split() ) )
gar=[]
shadow=[]
gar.append(a[0])
light=False #
a.append(m)
for i in range(1,n+1):
    dl=a[i]-a[i-1]
    if light:
        gar.append(dl)
        light=False
    else:
        shadow.append(dl)
        light=True
light=sum(gar)
dark=sum(shadow)
lightmax=light
teclight=0
tecdark=0
if n%2==0:
    n=n//2
else:
    n=n//2+1
for i in range(n):
    if i!=n-1:                         #!!!!!!!!!
        teclight+=gar[i]
        light-=gar[i]
        if gar[i]>1:
            newlight=teclight-1+dark
            lightmax=max(lightmax, newlight)
        tecdark+=shadow[i]
        dark-=shadow[i]
        if shadow[i]>1:
            newlight=teclight+shadow[i]-1+dark
            lightmax=max(lightmax, newlight)
    else:
        if len(shadow)==n:
            teclight+=gar[i]
            light-=gar[i]
            if gar[i]>1:
                newlight=teclight-1+dark
                lightmax=max(lightmax, newlight)
            tecdark+=shadow[i]
            dark-=shadow[i]
            if shadow[i]>1:
                newlight=teclight+shadow[i]-1+dark
                lightmax=max(lightmax, newlight)
print(lightmax)
            
        

