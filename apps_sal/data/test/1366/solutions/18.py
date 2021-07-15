def mainn():
    mode="filee"
    if mode=="file":f=open("test.txt","r")
    #f.readline()
    #input()
    get = lambda :[int(x) for x in (f.readline() if mode=="file" else input()).split()]
    [n]=get()
    found=[]
    opener=set()
    count=0
    other=[]
    for i in range(n):
        [a,b]=get()
        if a==b:
            found.append(a)
            other.append(b)
            continue
        found.append(a)
        opener.add(b)
    c=set(found)
    final=c-opener
    for i in final:
        count+=found.count(i)
    for i in other:
        count-=(found.count(i)-1)
    print(max(0,count))
    
    if mode=="file":f.close()

def __starting_point():
    mainn()

__starting_point()
