#
# Created by Daniil Kozhanov. All rights reserved.
#               december 2016

n = int(input())
s = input()
u = [1] * n
u1 = 0
u2 = 0
c1 = s.count("D")
c2 = s.count("R")

while c1 != 0 and c2 !=0:
    for i in range(n):
        if s[i] == "D":
            if u[i] == 1:
                if u1 > 0:
                    u1 -= 1
                    u[i] -= 1
                    c1 -= 1
                else:
                    u2 += 1
        else:
            if u[i] == 1:
                if u2 > 0:
                    u2 -= 1
                    u[i] -= 1
                    c2 -= 1
                else:
                    u1 += 1

if c2 == 0:
    print("D")
else:
    print("R")
