n = int(input())
for i in range(n):
    s = input()
    S = set(s)
    A = sorted(list(S))
    if len(S) == len(s) and ord(A[-1]) - ord(A[0]) == len(s) - 1:
        print('Yes')
    else:
        print('No')
