N = int(input())
S = input()

if N%2 == 1:
    print('No')
else:
    if S[0:N//2] == S[N//2:N]:
        print('Yes')
    else:
        print('No')

