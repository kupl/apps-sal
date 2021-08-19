# 昇順に並び替えてabcになったらYes

S = list(input())

S_ascending_order = ''.join(sorted(S))
# print(S_ascending_order)

if 'abc' == S_ascending_order:
    print('Yes')
else:
    print('No')
