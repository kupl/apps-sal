(A, B) = map(int, input().split())
S = input()
if S.find('-') == S.rfind('-') == A:
    print('Yes')
else:
    print('No')
