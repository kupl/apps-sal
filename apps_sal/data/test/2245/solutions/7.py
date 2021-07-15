def gns():
    return list(map(int,input().split()))
t=int(input())


def one():
    n,k=gns()
    if k%3!=0:
        if n%3==0:
            print('Bob')
        else:
            print('Alice')
        return
    if n%(k+1)==k:
        print('Alice')
        return
    n=n%(k+1)
    if n%3==0:
        print('Bob')
    else:
        print('Alice')



for i in range(t):
    one()





