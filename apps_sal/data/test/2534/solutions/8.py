# cook your dish here
r,c=list(map(int,input().split(" ")))

mat=[]
small_mat=[]
#slc=[]
result="GUESS"

for i in range(r):
    data=list(map(int,input().split(" ")))
    small_mat.append(min(data))
    mat.append(data)

#print(small_mat)

for i in range(r):
    for j in range(c):
        if mat[i][j]==small_mat[i]:
            temp_data=[]
            for k in range(r):
                temp_data.append(mat[k][j])
            
            if max(temp_data)==small_mat[i]:
                result=small_mat[i]
                break
print(result)
