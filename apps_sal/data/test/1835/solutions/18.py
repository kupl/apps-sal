"""
Created on 2019. 9. 21.

@author: kkhh88
"""
q = int(input())
for _ in range(q):
    n = int(input())
    l = [0] * n
    cnt0 = 0
    cnt1 = 0
    cntodd = 0
    for i in range(n):
        s = input()
        l[i] = len(s)
        if l[i] % 2 == 1:
            cntodd = cntodd + 1
        for c in s:
            if c == '0':
                cnt0 = cnt0 + 1
            else:
                cnt1 = cnt1 + 1
    if cnt0 % 2 == 1 and cntodd > 0:
        cnt0 = cnt0 - 1
        cntodd = cntodd - 1
    if cnt1 % 2 == 1 and cntodd > 0:
        cnt1 = cnt1 - 1
        cntodd = cntodd - 1
    if cnt0 % 2 == 1 or cnt1 % 2 == 1:
        print(n - 1)
    else:
        print(n)
