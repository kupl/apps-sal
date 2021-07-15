S = input()

if S[0] == S[-1]:  # 奇数手の負け
    if len(S) % 2 == 1:
        print('Second')
    else:
        print('First')
else:
    if len(S) % 2 == 0:
        print('Second')
    else:
        print('First')

