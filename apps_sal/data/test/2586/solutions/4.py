t=int(input())
for i in range(t):
    n, m =list(map(int, input().split()))
    print("W"+'B'*(m-1))
    for j in range(n-1):
        print('B'*m)

