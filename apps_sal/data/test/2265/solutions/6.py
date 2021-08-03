import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

C1 = b.count("1")

L = len(b)
C0 = (L - a[:L].count("0") + C1) % 2

ANS = 0
if C0 % 2 == 0:
    ANS += 1

for i in range(L, len(a)):
    if a[i] == "0":
        C0 += 1
    if a[i - L] == "0":
        C0 -= 1

    if C0 % 2 == 0:
        ANS += 1

print(ANS)
