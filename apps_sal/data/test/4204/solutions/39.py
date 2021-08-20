S = input()
K = int(input())
for i in range(len(S)):
    if S[i] == '1':
        pass
    else:
        break
if K < i + 1:
    print(1)
else:
    print(S[i])
