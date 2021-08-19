from math import log10
Ans = []
for i in range(int(input())):
    x = int(input())
    if x >= int(str(x)[0] * len(str(x))):
        Ans.append(int(log10(x)) * 9 + int(str(x)[0]) - 0)
    else:
        Ans.append(int(log10(x)) * 9 + int(str(x)[0]) - 1)
for a in Ans:
    print(a)
