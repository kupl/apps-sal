S = input()
ans = False
for i in range(len(S)):
    if S[1] == S[2] == S[3] or S[0] == S[1] == S[2]:
        ans = True
if ans:
    print("Yes")
else:
    print("No")
