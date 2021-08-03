# -*- coding:utf-8 -*-
a, b = input().split()

judge = int(a + b)

if any(i**2 == judge for i in range(judge // 2)):
    print("Yes")
else:
    print("No")
