import sys
input = sys.stdin.readline

n = int(input())
S = input().strip()

NOW = 0
LIST = []

for s in S:
    if s == "(":
        LIST.append(NOW)
        NOW += 1
    else:
        NOW -= 1
        LIST.append(NOW)

ANS = []

for l in LIST:
    if l % 2 == 0:
        ANS.append("0")
    else:
        ANS.append("1")

print("".join(ANS))
