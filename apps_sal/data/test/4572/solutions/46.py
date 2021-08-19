# -*- coding: utf-8 -*-

S = sorted(set(list(input())))

ans = 'None'
for keyword in list("abcdefghijklmnopqrstuvwxyz"):
    hit = False
    for s in S:
        if s == keyword:
            hit = True
            break

    if hit == False:
        ans = keyword
        break

print(ans)
