N = int(input())
A = [int(input()) for i in range(N)]
m = max(A)
mindex = A.index(m)
for i in range(N):
    if(i != mindex):
        print(m)
    else:
        pop = A.pop(i)
        print(max(A))
        A.insert(i,pop)
