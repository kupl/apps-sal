def Abs(a):
    if a<0:
        return -a
    return a


def main():
    x,y=[int(a) for a in input().split(' ')]
    val=Abs(x)+Abs(y)
    if(x<0 and y>0):
        print(-val,'0','0',val)
    if(x<0 and y<0):
        print(-val,'0','0',-val)
    if(x>0 and y>0):
        print('0',val,val,'0')
    if(x>0 and y<0):
        print('0',-val,val,'0')
        
main()
