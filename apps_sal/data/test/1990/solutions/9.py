import sys
input = sys.stdin.readline
N = int(input())
S = list(input().rstrip())
L = [0]
Lm = [0]
LM = [0]
R = [0]
Rm = [0]
RM = [0]
ans = []
for s in S:
    if s == 'R':
        if len(R) == 1:
            d = 0
        else:
            d = R[-2] - R[-1]
            R.pop()
            Rm.pop()
            RM.pop()
        L.append(L[-1] + d)
        Lm.append(min(Lm[-1], L[-1]))
        LM.append(max(LM[-1], L[-1]))
    elif s == 'L':
        if len(L) != 1:
            d = L[-2] - L[-1]
            L.pop()
            Lm.pop()
            LM.pop()
            R.append(R[-1] + d)
            Rm.append(min(Rm[-1], R[-1]))
            RM.append(max(RM[-1], R[-1]))
    else:
        if s == '(':
            num = -1
        elif s == ')':
            num = +1
        else:
            num = 0
        if len(R) != 1:
            R.pop()
            Rm.pop()
            RM.pop()
        R.append(R[-1] + num)
        Rm.append(min(Rm[-1], R[-1]))
        RM.append(max(RM[-1], R[-1]))
    if L[-1] == R[-1] and Lm[-1] >= 0 and (Rm[-1] >= 0):
        ans.append(str(max(LM[-1], RM[-1])))
    else:
        ans.append(str(-1))
print(' '.join(ans))
