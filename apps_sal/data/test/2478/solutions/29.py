N = int(input())
S = input()
left_cnt = 0
right_cnt = 0
for s in S:
    if s == '(':
        left_cnt += 1
    else:
        if left_cnt == 0:
            right_cnt += 1
        else:
            left_cnt -= 1
S = '(' * right_cnt + S + ')' * left_cnt
print(S)
