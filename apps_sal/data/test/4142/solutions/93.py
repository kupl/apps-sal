S = input()
l = len(S)
yes = True
for i in range(l):
    if i % 2:
        if S[i] == 'R':
            yes = False
    else:
        if S[i] == 'L':
            yes = False
if yes:
    print("Yes")
else:
    print("No")
