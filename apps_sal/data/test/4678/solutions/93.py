def steps():
    biggerone=0
    ans=0
    list_a=[]
    cnt=int(input())
    a=input()
    list_a=[int(x) for x in a.split()]
    if len(list_a)!=cnt:
        print('Wrong input')

        if ans==0:
            ans=None

        steps()

    else:

        for i in range(0,len(list_a)-1):
            if i ==0:
                biggerone=list_a[i]

            if biggerone>list_a[i+1]:
                ans+=biggerone-list_a[i+1]
            else:
                biggerone=list_a[i+1]

    print(ans)

steps()

