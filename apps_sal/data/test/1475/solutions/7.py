R = lambda : list(map(int, input().split()))
n,b,k,x = R()
v = list(R())
mod = 10**9+7

arr_0 = [0]*x
for bd in v:
    arr_0[bd%x]+=1

def cross(arr1,arr2,x,mod):
    arr = [0]*len(arr1)
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            arr[(i+j)%x] += arr1[i]*arr2[j]
    for i in range(len(arr)):
        arr[i] %= mod
    return arr

def move(arr,s,x):
    m = pow(10,s,x)
    res = [0]*x
    for i in range(x):
        res[(i*m)%x]+=arr[i]
    return res

def solve(b,x,arr_0,mod):
    if b==1:
        return arr_0
    if b%2==1:
        sol = solve(b-1,x,arr_0,mod)
        return cross(move(sol,1,x),arr_0,x,mod)
    else:
        sol = solve(b//2,x,arr_0,mod)
        return cross(move(sol,b//2,x),sol,x,mod)

sol = solve(b,x,arr_0,mod)
print(sol[k])


