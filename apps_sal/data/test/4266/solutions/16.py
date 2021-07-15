a = list(map(int,input().split()))
K = a[0]
X = a[1]

for i in range(2*K-1):
    print(X-(K-1)+i, end = " ")
