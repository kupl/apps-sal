def takeinput():
    b,g = list(map(int,input().split()))
    boy = [0]*b
    girl = [0]*g
    ans = [] 
    sum = -1
    for i in range(b):
        for j in range(g):
            if boy[i]==0 or girl[j]==0:
                temp = i+j
                if temp>sum:
                    boy[i]=1
                    girl[j]=1
                    sum=temp
                    ans.append((i+1,j+1))
    return ans

def __starting_point():
    res = takeinput()
    print(len(res))
    for val in res:
        print(val[0],val[1])


__starting_point()
