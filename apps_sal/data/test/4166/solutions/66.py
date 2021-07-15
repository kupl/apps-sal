from random import randint

def getrand():
    n = randint(1,3)
    m = randint(0,5)
    s = []
    for i in range(m):
        s.append([randint(1,n),randint(0,9)])
    s.sort()
    print([n,m])
    print(s)
    return n,m,s

def getval():
    n,m = list(map(int,input().split()))
    s = [list(map(int,input().split())) for i in range(m)]
    return n,m,s

def getrand():
    n = randint(1,3)
    m = randint(0,5)
    s = []
    for i in range(m):
        s.append([randint(1,n),randint(0,9)])
    s.sort()
    print([n,m])
    print(s)
    return n,m,s

def getval():
    n,m = list(map(int,input().split()))
    s = [list(map(int,input().split())) for i in range(m)]
    return n,m,s

def main(n,m,s):
    #Initiate
    temp = [-1 for i in range(n)]
    ans = ""
    flag = True
    #Exceptions: contains dup or ([1,0] and n>1)
    if [1,0] in s and n>1:
        flag = False
    for i in s:
        if not temp[i[0]-1] in [-1,i[1]]:
            flag = False
            break
        temp[i[0]-1] = i[1]
    if flag:
        if n==1:
            if m==0:
                ans = "0"
            else:
                ans = str(temp[0])
        else:
            if temp[0]==-1:
                temp[0] = 1
            for i in range(0,n):
                if temp[i]==-1:
                    temp[i] = 0
            for i in temp:
                ans += str(i)
    else:
        ans = "-1"
    print(ans)
        

def __starting_point():
    #n,m,s = getrand()
    n,m,s = getval()
    main(n,m,s)
    #for i in range(10):
      #n,m,s = getrand()
      #main(n,m,s)

__starting_point()
