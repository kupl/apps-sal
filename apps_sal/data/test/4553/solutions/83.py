(A, B) = map(int, input().split())
S = input()
flag = True
for i in range(A + B + 1):
    if i == A:
        if S[i] != '-':
            flag = False
    elif S[i] == '-':
        flag = False
if flag:
    print('Yes')
else:
    print('No')
