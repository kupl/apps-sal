S = list(input())
T = list(input())
match = 0
for _ in S:
    i = S.pop()
    S.insert(0, i)
    ''.join(S)
    if S == T:
        match += 1
        break
if match == 0:
    print('No')
else:
    print('Yes')
