A, B = map(int, input().split())
d = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
S = input()
total = 0
for i in range(A):
    if S[i] in d:
        pass
    else:
        total = 1
S = S[A:]
if S[0] != "-":
    total = 1
S = S[1:]
for i in range(B):
    if S[i] in d:
        pass
    else:
        total = 1
if total == 1:
    print("No")
else:
    print("Yes")
