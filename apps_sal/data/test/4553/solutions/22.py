A, B = map(int, input().split())
S = input()

flag = False
if S[A] == '-':
    S_ = S.split('-')
    if len(S_) == 2:
        if len(S_[0]) == A and len(S_[1]) == B:
            if S_[0].isdigit() and S_[1].isdigit():
                flag = True

if flag:
    print('Yes')
else:
    print('No')
