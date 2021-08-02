# -*- coding: utf-8 -*-
a = list(map(int, input().split()))
if sum(a) <= 21:
    print('win')
else:
    print('bust')
