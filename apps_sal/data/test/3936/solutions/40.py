#!/usr/bin/env python3
n = int(input())
s = [input() for _ in range(2)]
mod = 10 ** 9 + 7
""" 
たて*たて = *2
たて*よこ = *2
よこ*よこ = *3 (1,2)=(2,3)(2,1),(3,1)
よこ*たて = *1
"""
tmp = 1
pos = 0  # 移動させる
pre_state = -1  # 0:tate 1:yoko
while pos < n:
    if s[0][pos] == s[1][pos]:
        if pos == 0:
            tmp *= 3
        else:
            if pre_state == 0:
                tmp *= 2
            else:
                tmp *= 1
        pre_state = 0
        pos += 1
    else:
        if pos == 0:
            tmp *= 6
        else:
            if pre_state == 0:
                tmp *= 2
            else:
                tmp *= 3
        pre_state = 1
        pos += 2
    tmp %= mod
print(tmp)
