a = list(map(int,input().split()))
A = a[0]
B = a[1]

print(max((A+B),(A-B),A*B))
