N = int(input())
S = str(input())
flag = False
half = (N + 1) // 2
if S[:half] == S[half:N]:
    flag = True
if flag:
    print('Yes')
else:
    print('No')
