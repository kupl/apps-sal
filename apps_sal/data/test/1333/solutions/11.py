N,M=list(map(int,input().split()))
R=True
for I in range(N):
    if (I+1)%2:
        print('#'*M)
    else:
        if R:
            print('.'*(M-1)+'#')
            R=False
        else:
            print('#'+'.'*(M-1))
            R=True

