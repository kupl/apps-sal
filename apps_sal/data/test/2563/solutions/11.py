"""
Created on 2019. 9. 21.

@author: kkhh88
"""
q = int(input())
for _ in range(q):
    s0 = ''
    s1 = ''
    s = input()
    ans = ''
    for c in s:
        if ord(c) % 2 == 1:
            s1 = s1 + c
        else:
            s0 = s0 + c
    l0 = 0
    l1 = 0
    while len(s0) > l0 and len(s1) > l1:
        if s0[l0] > s1[l1]:
            ans = ans + s1[l1]
            l1 = l1 + 1
        else:
            ans = ans + s0[l0]
            l0 = l0 + 1
    print(ans + s1[l1:] + s0[l0:])
