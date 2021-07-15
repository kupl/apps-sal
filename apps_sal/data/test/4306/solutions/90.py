A, B, C, D = map(int,input().split())

if C >= B or A >= D:
    print("0")

else:
    mi = max(A,C)
    ma = min(B,D)
    print(ma - mi)
