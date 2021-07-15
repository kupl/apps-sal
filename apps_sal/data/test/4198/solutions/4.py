A,B,X = list(map(int,input().split()))
right = 10**9
left = 0
while abs(right-left)>1:
    N = (left + right)//2
    cal = N * A + len(str(N)) * B
    if cal == X:
        ans = N
        print(ans)
        break
    elif cal < X:
        left = N 
    else:
        right = N
else:
    if  A * right + len(str(right)) * B <= X:
        print(right)
    else:
        print(left)

