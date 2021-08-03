A, B = map(int, input().split())
S = input()
for i in range(A + B + 1):
    if i < A and S[i] == '-':
        print('No')
        return
    elif i == A and S[i] != '-':
        print('No')
        return
    elif i > A and S[i] == '-':
        print('No')
        return
print('Yes')
