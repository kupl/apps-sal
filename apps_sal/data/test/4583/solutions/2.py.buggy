# -*- coding: utf-8 -*-

num = list(input())

op = ['+', '-']

for op1 in op:
    if op1 == '+':
        res1 = int(num[0]) + int(num[1])
    else:
        res1 = int(num[0]) - int(num[1])
    for op2 in op:
        if op2 == '+':
            res2 = res1 + int(num[2])
        else:
            res2 = res1 - int(num[2])
        for op3 in op:
            if op3 == '+':
                res3 = res2 + int(num[3])
            else:
                res3 = res2 - int(num[3])

            if res3 == 7:
                ans = num[0] + op1 + num[1] + op2 + num[2] + op3 + num[3] + "=7"
                print(ans)
                return
