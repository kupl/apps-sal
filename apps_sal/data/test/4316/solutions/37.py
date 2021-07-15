import sys

S = list(sys.stdin.readline().strip())
S.sort()
if S[0] == S[1] and S[2] == S[3] and S[0] != S[2]:
    print("Yes")
else:
    print("No")
