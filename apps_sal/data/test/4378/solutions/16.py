import sys
input = sys.stdin.readline
n = int(input())
S = list(input())
ANS = 0
LIST = ['R', 'G', 'B']
for i in range(1, n):
    if S[i] == S[i - 1]:
        if i < n - 1:
            for l in LIST:
                if S[i - 1] != l and S[i + 1] != l:
                    ANS += 1
                    S[i] = l
                    break
        else:
            for l in LIST:
                if S[i - 1] != l:
                    ANS += 1
                    S[i] = l
                    break
print(ANS)
print(''.join(S))
