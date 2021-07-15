from re import *
def main():
    mode="filee"
    if mode=="file":f=open("test.txt","r")
    #f.readline()
    #input()
    get = lambda :[f.readline()[:-1] if mode=="file" else input()]
    for z in range(8):
        q=get()
        q=q[0]
        if search('BB',q)!=None or search('WW',q)!=None:
            print("NO")
            return
    print("YES")
    


    if mode=="file":f.close()


def __starting_point():
    main()

__starting_point()
