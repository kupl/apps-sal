a,b,k = map(int,input().split())
if 2*k > b - a:
    for i in range(a,b + 1):
        print(i)
else:
    for i in range(k):
        print(a + i)
    for j in range(k):
        print(b - k + 1 + j)
