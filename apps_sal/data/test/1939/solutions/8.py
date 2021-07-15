n, k = map(int, input().split())
for i in range (n):
    for j in range (n):
        print([0,k][i==j],end=" ")
    print()

