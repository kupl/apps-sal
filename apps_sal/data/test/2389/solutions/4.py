#F
import sys
from collections import Counter as cc

N,A,B,C = list(map(int, input().split()))
abc = []
ans = []

for i in range(N):
    abc.append(input())
abc.append("")

a = abc.count("AB")+abc.count("AC")
b = abc.count("AB")+abc.count("BC")
c = abc.count("AC")+abc.count("BC")


for i, (s, ns) in enumerate(zip(abc,abc[1:])):
    if s == "AB":
        if A > B or (A == B and i != N-1 and ("AB" in ns or "BC" in ns)):
            A -= 1
            B += 1
            ans.append("B")
        else:
            A += 1
            B -= 1
            ans.append("A")
    elif s == "AC":
        a -= 1
        c -= 1
        if A > C or (A == C and i != N-1 and ("AC" in ns or "BC" in ns)):
            A -= 1
            C += 1
            ans.append("C")
        else:
            A += 1
            C -= 1
            ans.append("A")
    else:
        c -= 1
        b -= 1
        if B > C or (B == C and i != N-1 and ("AC" in ns or "BC" in ns)):
            C += 1
            B -= 1
            ans.append("C")
        else:
            C -= 1
            B += 1
            ans.append("B")
    if A < 0 or B < 0 or C < 0:
        print("No")
        return

print("Yes")
for i in range(N):
    print(str(ans[i]))
