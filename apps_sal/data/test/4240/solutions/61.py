S = input()
T = input()
success = 0
for i in range(len(S)):
    if S[i:] + S[:i] == T:
        success += 1
if success >= 1:
    print('Yes')
else:
    print('No')
