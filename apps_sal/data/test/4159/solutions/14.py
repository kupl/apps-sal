A,B,K = map(int,input().split())

A,rem = max(A-K,0),max(K-A,0)
B = max(B-rem,0)

print(A,B)
