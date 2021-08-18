#!/usr/bin/env python3
def ri():
    return map(int, input().split())


n = int(input())
a = ri()

b = set()

s = n

for aa in a:
    b.add(aa)
    if aa == s:
        print(s, end="")
        for ss in range(s - 1, 0, -1):
            if ss == 0:
                print()
                return
            if ss in b:
                print(" ", end="")
                print(ss, end="")
            else:
                s = ss
                print()
                break
    else:
        print()

print()
