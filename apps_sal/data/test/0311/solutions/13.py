x,y,z,t1,t2,t3=map(int,input().split())
if abs(x-y)*t1>=abs(x-z)*t2+t3*3+abs(x-y)*t2:
    print('YES')
else:
    print('NO')
