import sys


def LI():
    return list(map(int, input().split()))


A, B = LI()
S = input()
ans = "Yes"
for i in range(A):
    if S[i] == "-":
        ans = "No"
        break
if S[A] != "-":
    ans = "No"
for i in range(A + 1, A + B + 1):
    if S[i] == "-":
        ans = "No"
        break
print(ans)
