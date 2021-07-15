n, m = list(map(int,input().split()))
matrix = [0] * n
ok = 0
for q in range(0,n):
    row = list(map(int,input().split()))
    matrix[q] = row

zero = 0
# def when_no_zero(n,m):
#     print("n",n,"m",m)
#     for z in range(0,n-1):
#         for x in range(0,m-1):
#             if(matrix[z][x]<matrix[z][x+1] and matrix[z][x]<matrix[z+1][x]):
#                 pass
#             else:
#                 print("-1")
#                 ok = 1
#                 break

def no_zeros(n,m):
    for g in range(0,n):
        for k in range(0,m-1):
            if(matrix[g][k]<matrix[g][k+1]):
                pass
            else:
                return -1
    for l in range(0,m-1):
        for m in range(0,n):
            if(matrix[l][m]<matrix[l+1][m]):
                pass
            else:
                return -1
    return find_sum(matrix)

def find_zero_value():
    for i in range(n-1,0,-1):
        for j in range(m-1,0,-1):
            if matrix[i][j] == 0:
                right = matrix[i][j+1]
                down = matrix[i+1][j]
                op_min = min([right,down])
                up = matrix[i-1][j]
                left = matrix[i][j-1]
                op_max = max([up,left])
                if(op_min-1>op_max):
                    matrix[i][j] = op_min-1
                else:
                    return -1
    return matrix
            
def find_sum(maz):
    su = 0
    for i in range(0,n):
        for j in range(0,m):
            su = su + matrix[i][j]
    return su


for i in range(0,n):
    for j in range(0,m):
        if matrix[i][j] == 0:
            zero = 1
            break

if(zero==0):
    print(no_zeros(n,m))
else:
    maz = find_zero_value()
    if(maz == -1):
        print("-1")
    else:
        summ = find_sum(maz)
        print(summ)

