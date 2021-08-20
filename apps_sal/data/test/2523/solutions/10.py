import sys
readline = sys.stdin.readline
S = readline().rstrip()
ans = len(S)
for i in range(1, len(S)):
    if S[i] != S[i - 1]:
        longer = max(i, len(S) - i)
        if ans > longer:
            ans = longer
print(ans)
