s=set()
sc=set()
t=set()
tc=set()
ms=[]
mt=[]
for letter in input():
    if letter==letter.lower():
        s.add(letter)
    else:
        sc.add(letter.lower())
    if letter not in ms:
        ms.append(letter)
        ms.append(1)
    else:
        ms[ms.index(letter)+1]+=1
for letter in input():
    if letter==letter.lower():
        t.add(letter)
    else:
        tc.add(letter.lower())
    if letter not in mt:
        mt.append(letter)
        mt.append(1)
    else:
        mt[mt.index(letter)+1]+=1
y=0
w=0
for letter in s.intersection(t):
    a=ms[ms.index(letter)+1]
    b=mt[mt.index(letter)+1]
    rs=set()
    rt=set()
    if a==b:
        y+=a
        ms[ms.index(letter)+1],mt[mt.index(letter)+1]=0,0
        rs.add(letter)
        rt.add(letter)
    elif a>b:
        y+=b
        ms[ms.index(letter)+1],mt[mt.index(letter)+1]=ms[ms.index(letter)+1]-mt[mt.index(letter)+1],0
        rt.add(letter)
    else:
        y+=a
        ms[ms.index(letter)+1],mt[mt.index(letter)+1]=0,mt[mt.index(letter)+1]-ms[ms.index(letter)+1]
        rs.add(letter)
    s,t=s-rs,t-rt
for letter in sc.intersection(tc):
    letter=letter.upper()
    a=ms[ms.index(letter)+1]
    b=mt[mt.index(letter)+1]
    rsc=set()
    rtc=set()
    if a==b:
        y+=a
        ms[ms.index(letter)+1],mt[mt.index(letter)+1]=0,0
        rsc.add(letter.lower())
        rtc.add(letter.lower())
    elif a>b:
        y+=b
        ms[ms.index(letter)+1],mt[mt.index(letter)+1]=ms[ms.index(letter)+1]-mt[mt.index(letter)+1],0
        rtc.add(letter.lower())
    else:
        y+=a
        ms[ms.index(letter)+1],mt[mt.index(letter)+1]=0,mt[mt.index(letter)+1]-ms[ms.index(letter)+1]
        rsc.add(letter.lower())
    sc,tc=sc-rsc,tc-rtc
for letter in sc.intersection(t):
    a=ms[ms.index(letter.upper())+1]
    b=mt[mt.index(letter)+1]
    rsc=set()
    rt=set()
    if a==b:
        w+=a
        rsc.add(letter)
        rt.add(letter)
    elif a>b:
        w+=b
        rt.add(letter)
    else:
        w+=a
        rsc.add(letter)
    sc,t=sc-rsc,t-rt
for letter in s.intersection(tc):
    a=ms[ms.index(letter)+1]
    b=mt[mt.index(letter.upper())+1]
    rs=set()
    rtc=set()
    if a==b:
        w+=a
        rs.add(letter)
        rtc.add(letter)
    elif a>b:
        w+=b
        rtc.add(letter)
    else:
        w+=a
        rs.add(letter)
    s,tc=s-rs,tc-rtc
print(y,w)
