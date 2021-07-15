n, m, x, y = list(map(int, input().split()))
print(x, y)
print(1, y)
for i in range(1, m+1):
    if i!=y:
        print(1, i)
curr = 0
for i in range(2, n+1):
    if curr%2==0:
        for j in range(m, 0,-1):
            if i!=x or j!=y:
                print(i, j)
    else:
        for j in range(1, m+1):
            if i!=x or j!=y:
                print(i, j)
    curr+=1

