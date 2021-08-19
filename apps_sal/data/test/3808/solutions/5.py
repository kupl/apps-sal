import sys
input = sys.stdin.readline
n = int(input())
S = input().strip()
NOW = 0
SC = []
for s in S:
    if s == '(':
        NOW += 1
    else:
        NOW -= 1
    SC.append(NOW)
if SC[-1] == 0 and min(SC) >= -1:
    print('Yes')
else:
    print('No')
