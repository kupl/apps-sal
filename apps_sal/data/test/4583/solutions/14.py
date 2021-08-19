from itertools import combinations
s = input()
ans = ['-', '-', '-']
for i in range(4):
    for comb in combinations(range(3), i):
        temp = int(s[0])
        for j in range(3):
            if j in comb:
                temp += int(s[j + 1])
            else:
                temp -= int(s[j + 1])
        if temp == 7:
            for j in comb:
                ans[j] = '+'
            break
print('{a}{op1}{b}{op2}{c}{op3}{d}=7'.format(a=s[0], op1=ans[0], b=s[1], op2=ans[1], c=s[2], op3=ans[2], d=s[3]))
