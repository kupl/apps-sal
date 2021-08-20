(A, B, C) = map(int, input().split())
print('No') if A == B and B == C or (A != B and B != C and (C != A)) else print('Yes')
