N,A,B=map(int, input().split())
print(A*(N//(A+B))+ (A if N%(A+B)>A else N%(A+B)))
