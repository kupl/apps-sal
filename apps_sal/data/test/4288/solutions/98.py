A, B, C = map(int, input().split())
if (A == B and B != C) or (A == C and B != A) or (B == C and B != A):
    print("Yes")
else:
    print("No")
