t= int(input())
for _ in range(t):
    n, x = list(map(int, input().split()))
    A = list(map(int, input().split()))
    odd = 0
    even = 0
    for i in range(n):
        if A[i]%2 == 1:
            odd += 1
        else:
            even += 1
    flag =False
    for j in range(x+1):
        if j%2 == 1 and j <= odd and (x-j) <= even:
            flag = True
            break
    if flag:
        print('Yes')
    else:
        print('No')

