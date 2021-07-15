s1=input().strip()
s2=input().strip()
h1=int(s1[:2])
h2=int(s2[:2])
m1=int(s1[3:])
m2=int(s2[3:])
h3=h1-h2
m3=m1-m2
if m3<0:
    m3=60+m3
    h3-=1
if h3<0:
    h3=24+h3
print((2-len(str(h3)))*'0'+str(h3)+':'+(2-len(str(m3)))*'0'+str(m3))

