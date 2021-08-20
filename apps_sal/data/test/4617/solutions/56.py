C1 = str(input())
C2 = str(input())
ori_str = C1 + C2
rev_str = ori_str[-1::-1]
if ori_str == rev_str:
    print('YES')
else:
    print('NO')
