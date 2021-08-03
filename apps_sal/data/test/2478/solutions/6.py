import sys
input = sys.stdin.readline

n = int(input())
S = input().rstrip()
b = 0
q = 0

for s in S:
    if s == '(':
        b += 1
    else:
        if b > 0:
            b -= 1
        else:
            q += 1
print(('(' * q + S + ')' * b))
