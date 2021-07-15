A, B, C, D = list(map(int, input().split()))
if A <= C:
    ans = min(B-C, D-C)
else:
    ans = min(D-A, B-A)
print((max(0,ans)))

