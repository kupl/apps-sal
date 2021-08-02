A, B = list(map(int, input().split()))
S = input()

if S[A] == '-' and '-' not in S[:A] and '-' not in S[-B:]:
    print('Yes')
else:
    print('No')
