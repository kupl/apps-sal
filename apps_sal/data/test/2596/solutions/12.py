nkmt=[int(k) for k in input().split()]
n= nkmt[0]
k = nkmt[1]
m = nkmt[2]
t = nkmt[3]
arr_d=[]
uni=[0] * n
uni[k - 1] = 1 
for _ in range(t):
    i = [int(k) for k in input().split()]
    
    if i[0]==1:
        uni.insert(i[1]-1,0)
    if i[0]==0:
        uni_temp1=uni[:i[1]]
        uni_temp2=uni[i[1]:]
        if 1 in uni_temp1:
            uni=uni_temp1
        else:
            uni=uni_temp2
    print(len(uni), end=' ')
    print(uni.index(1)+1)   
        


