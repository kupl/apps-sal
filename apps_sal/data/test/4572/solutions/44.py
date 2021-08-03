# -*- coding: utf-8 -*-

S = set(input())
az = [chr(i) for i in range(ord('a'), ord('z') + 1)]

if len(S) >= 26:
    print("None")
    return

for i in az:
    if i in S:
        pass
    else:
        print(i)
        return
