s = input();n=len(s)
def i(c,o=0): 
    try: return s[::-1].index(str(c),o)
    except: return -1
oo=0
while oo<n-1 and s[oo+1]=='0':oo+=1
o5=i(5)
o7=i(7)
o2=i(2)
o01=i(0);o02=i(0,o01+1) if o01>=0 else -1
r=100
if o01>=0 and o02>=0: r=min(r,o01+o02-1)
if o01>=0 and o5>=0: r=min(r,o01+o5-int(o01<o5))
if o5>=0 and o2>=0: r=min(r,o5+o2-int(o5<o2)+int(o5==n-1 and oo))
if o5>=0 and o7>=0: r=min(r,o5+o7-int(o5<o7)+int(o5==n-1 and oo))
print(r if r<100 else -1)

