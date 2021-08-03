import io
import os
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def R(): return map(int, input().split())


for _ in range(int(input())):
    n = int(input())
    a = list(R())
    a.sort()
    can = False
    val = {}
    for i in a:
        if i not in val:
            val[i] = 1
        else:
            val[i] += 1
    if n & 1 or all(v % 2 == 0 for k, v in val.items()):
        print("Second")
    else:
        print("First")
