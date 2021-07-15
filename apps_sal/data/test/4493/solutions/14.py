x=list(map(int, input().split()))
y=list(map(int, input().split()))
z=list(map(int, input().split()))
if x[1]-x[0] != y[1]-y[0] or y[1]-y[0] != z[1]-z[0] or x[2]-x[0] != y[2]-y[0] or y[0]-x[0] !=y[1]-x[1] or z[1]-x[1] !=z[2]-x[2] or z[0]-x[0] !=z[1]-x[1] or z[1]-x[1] !=z[2]-x[2] :
    print('No')
else:
    print('Yes')
