N = int(input())
S = str(input())
half = (N + 1) // 2
if N % 2 != 0:
    if S[:half] == S[half + 1:N]:
        print('Yes')
    else:
        print('No')
elif S[:half] == S[half:N]:
    print('Yes')
else:
    print('No')
