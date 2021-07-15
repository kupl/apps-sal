A, B, C = map(int, input().split())

S = ((A*(A+1))//2)*((B*(B+1))//2)*((C*(C+1))//2)
print(S%998244353)
