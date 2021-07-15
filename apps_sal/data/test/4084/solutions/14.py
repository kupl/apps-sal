N, A, B = map(int, input().split())
q = N//(A+B)
print(q*A+min(A, N-(A+B)*q))
