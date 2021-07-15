# -*- coding:utf-8 -*-
import re
S = input()
S_sp = re.split("[^ACGT]",S)
ans = 0
for moji in S_sp:
    if len(moji) > ans:
        ans = len(moji) 

print(ans)

