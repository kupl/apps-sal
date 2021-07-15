
A, B = list(map(int, input().split()))
S = input()

if len(S) != A+B+1:
    print("No")
    return

for i in range(A+B+1):

    if i == A:
        if S[i] != "-":
            print('No')
            return
    else:
        if not('0' <= S[i] <= '9'):
            print('No')
            return
print('Yes')

